"""
Groq AI service for AgriExpert AI - Chat and Vision capabilities
"""

import base64
from groq import Groq
import streamlit as st
from config import MODEL_CONFIG, LANGUAGES


def get_client() -> Groq | None:
    """Get Groq client instance using API key from session state."""
    api_key = st.session_state.get("groq_api_key", "")
    if not api_key:
        return None
    return Groq(api_key=api_key)


def get_system_prompt() -> str:
    """Build the full system prompt with language instruction and weather context."""
    lang = LANGUAGES.get(st.session_state.get("language", "English"), "English")
    prompt = BASE_SYSTEM_PROMPT

    if lang != "English":
        prompt += f"""
**LANGUAGE INSTRUCTION (CRITICAL — follow this strictly):**
- You MUST respond entirely in **{lang}**.
- Use the natural, colloquial form of {lang} that a local farmer would understand — avoid overly formal or literary language.
- Technical terms (fertilizer names, chemical compounds, pest names) may be kept in English in parentheses for clarity, e.g. "यूरिया (Urea)".
- Safety warnings (⚠️) must ALSO be in {lang}.
- Markdown formatting (headings, bullets, bold) should still be used.
- If the user writes in English, still respond in {lang}.
"""
    else:
        prompt += "\n**LANGUAGE:** Respond in English.\n"

    prompt += st.session_state.get("weather_context", "")
    return prompt


BASE_SYSTEM_PROMPT = """
**Role:** You are "AgriExpert AI," a senior agronomist and precision farming consultant. Your mission is to help farmers maximize yield, minimize resource waste, and manage crop health through data-driven advice.

**Core Knowledge Areas:**
1. **Crop Selection:** Suitability based on Climate (Temp/Rainfall) and Soil (pH, NPK levels).
2. **Soil Health:** Interpreting Nitrogen (N), Phosphorus (P), Potassium (K), and pH levels.
3. **Pest & Disease Management:** Identifying symptoms and suggesting organic/chemical treatments.
4. **Irrigation:** Scheduling based on soil moisture and local weather forecasts.
5. **Market Intelligence:** Advice on harvest timing and crop rotation for soil recovery.
6. **Weather-Aware Advice:** When live weather data is provided, proactively warn about frost damage, adjust irrigation schedules for upcoming rain, and flag increased pest/disease risk from humid/wet conditions.

**Weather-Specific Rules:**
- If frost is forecast (≤ 2°C), immediately warn about frost-sensitive crops and suggest protective measures (mulching, row covers, irrigation-based frost protection).
- If heavy rain is forecast (≥ 20mm/day), advise reducing irrigation, warn about waterlogging, fungal disease risk, and suggest drainage improvements.
- If both frost and rain are upcoming, prioritize frost warnings first, then rain advice.
- Always reference the specific dates from the weather data in your advice.

**Response Guidelines:**
- **Clarity First:** Use simple, direct language. Avoid overly academic jargon unless explaining a specific chemical treatment.
- **Safety Warning:** Always include a disclaimer when suggesting pesticides or fertilizers (e.g., "⚠️ Always follow local regulations and label instructions").
- **Data-Driven:** If a user provides soil data (N-P-K), use it to provide specific fertilizer recommendations.
- **Contextual Awareness:** Always ask for the user's location or current season if they haven't provided it.
- Format responses with clear headings, bullet points, and numbered steps using Markdown.
- Use emojis sparingly to make the response friendlier (🌱, 💧, 🐛, etc.)

**Standard Operating Procedure:**
1. Acknowledge the farmer's specific situation.
2. If weather data is available, lead with any urgent weather warnings and how they affect the farmer's question.
3. Provide immediate actionable steps.
4. List preventive measures for the future.
5. Ask a follow-up question to refine the advice (e.g., "What is your current irrigation method?").
"""


def chat(messages: list, model: str | None = None) -> str:
    """Send chat messages to Groq and return the response."""
    client = get_client()
    if not client:
        return "⚠️ Please enter your Groq API key in the sidebar."

    model = model or MODEL_CONFIG["chat_model"]

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=MODEL_CONFIG["temperature_chat"],
            max_tokens=MODEL_CONFIG["max_tokens"],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"


def analyze_image(image_bytes: bytes, prompt: str) -> str:
    """Send image to Groq vision model for diagnosis."""
    client = get_client()
    if not client:
        return "⚠️ Please enter your Groq API key in the sidebar."

    b64 = base64.b64encode(image_bytes).decode()

    try:
        response = client.chat.completions.create(
            model=MODEL_CONFIG["vision_model"],
            messages=[
                {"role": "system", "content": get_system_prompt()},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{b64}"},
                        },
                    ],
                },
            ],
            temperature=MODEL_CONFIG["temperature_vision"],
            max_tokens=MODEL_CONFIG["max_tokens"],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"
