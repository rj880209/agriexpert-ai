"""
AgriExpert AI — Smart Farming Assistant
Built with Streamlit + Groq AI
Includes real-time weather alerts (frost & heavy rain) via Open-Meteo API
"""

import streamlit as st
from groq import Groq
import base64
import json
import requests
from datetime import datetime, timedelta

# ─── Page Config ─────────────────────────────────────────────
st.set_page_config(
    page_title="AgriExpert AI — Smart Farming Assistant",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS — Earthy Farming Aesthetic ───────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Source+Sans+3:wght@400;500;600;700&display=swap');

    :root {
        --soil-dark: #3E2723;
        --soil-medium: #5D4037;
        --soil-light: #8D6E63;
        --leaf-dark: #2E7D32;
        --leaf-medium: #43A047;
        --leaf-light: #66BB6A;
        --wheat-gold: #F9A825;
        --wheat-light: #FDD835;
        --sunrise-orange: #EF6C00;
        --sky-blue: #0288D1;
        --cream: #FFF8E1;
        --warm-white: #FFFDF5;
        --parchment: #F5F0E1;
        --field-green: #E8F5E9;
    }

    /* Global */
    * { font-family: 'Source Sans 3', sans-serif; }
    h1, h2, h3, h4, h5, h6 { font-family: 'Merriweather', serif !important; }

    .stApp {
        background: linear-gradient(180deg, var(--warm-white) 0%, var(--parchment) 40%, #E8E0D0 100%);
    }

    /* ── Sidebar ── */
    div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--soil-dark) 0%, var(--soil-medium) 100%) !important;
    }
    div[data-testid="stSidebar"] * {
        color: var(--cream) !important;
    }
    div[data-testid="stSidebar"] .stSelectbox label,
    div[data-testid="stSidebar"] .stTextInput label {
        color: var(--wheat-light) !important;
        font-weight: 600 !important;
    }
    div[data-testid="stSidebar"] .stRadio label {
        color: var(--cream) !important;
    }
    div[data-testid="stSidebar"] input,
    div[data-testid="stSidebar"] select {
        background: rgba(255,255,255,0.1) !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        color: white !important;
    }
    div[data-testid="stSidebar"] .stButton button {
        background: linear-gradient(135deg, var(--leaf-dark), var(--leaf-medium)) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: all 0.3s !important;
    }
    div[data-testid="stSidebar"] .stButton button:hover {
        background: linear-gradient(135deg, var(--leaf-medium), var(--leaf-light)) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(46,125,50,0.4) !important;
    }
    div[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.15) !important;
    }

    /* ── Main Header ── */
    .main-header {
        background: linear-gradient(135deg, var(--soil-dark) 0%, var(--soil-medium) 40%, var(--leaf-dark) 100%);
        padding: 2.5rem 3rem;
        border-radius: 20px;
        color: white;
        margin-bottom: 1.5rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(62,39,35,0.3);
    }
    .main-header::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, rgba(249,168,37,0.15) 0%, transparent 70%);
        border-radius: 50%;
    }
    .main-header::after {
        content: '🌾🌱🌿';
        position: absolute;
        bottom: 10px;
        right: 20px;
        font-size: 2rem;
        opacity: 0.2;
        letter-spacing: 8px;
    }
    .main-header h1 {
        margin: 0;
        font-size: 2.4rem;
        font-weight: 900;
        font-family: 'Merriweather', serif !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        letter-spacing: -0.5px;
    }
    .main-header p {
        margin: 0.5rem 0 0;
        opacity: 0.9;
        font-size: 1.1rem;
        font-weight: 400;
        letter-spacing: 0.3px;
    }
    .main-header .tagline {
        display: inline-block;
        background: rgba(249,168,37,0.25);
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-top: 0.8rem;
        letter-spacing: 1px;
        text-transform: uppercase;
        border: 1px solid rgba(249,168,37,0.3);
    }

    /* ── Feature Cards ── */
    .feature-card {
        background: var(--warm-white);
        border: 2px solid #E0D5C1;
        border-radius: 16px;
        padding: 1.5rem 1.2rem;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(93,64,55,0.08);
        position: relative;
        overflow: hidden;
    }
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--leaf-dark), var(--wheat-gold));
    }
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px rgba(93,64,55,0.15);
        border-color: var(--leaf-medium);
    }
    .feature-card .icon { font-size: 2.5rem; margin-bottom: 0.8rem; }
    .feature-card h4 {
        margin: 0;
        color: var(--soil-dark);
        font-family: 'Merriweather', serif !important;
        font-size: 1rem;
        font-weight: 700;
    }
    .feature-card p {
        margin: 0.4rem 0 0;
        font-size: 0.82rem;
        color: var(--soil-light);
        line-height: 1.4;
    }

    /* ── Chat Bubbles ── */
    div[data-testid="stChatMessage"] {
        border-radius: 16px !important;
        margin-bottom: 0.8rem !important;
    }
    .chat-user {
        background: linear-gradient(135deg, #FFF8E1, #FFF3CD);
        border: 1px solid #E0D5C1;
        border-radius: 16px 16px 4px 16px;
        padding: 1rem 1.2rem;
        margin: 0.5rem 0;
        max-width: 80%;
        margin-left: auto;
    }
    .chat-assistant {
        background: var(--warm-white);
        border: 1px solid #D7CCC8;
        border-left: 4px solid var(--leaf-dark);
        border-radius: 16px 16px 16px 4px;
        padding: 1rem 1.2rem;
        margin: 0.5rem 0;
        max-width: 85%;
    }

    /* ── Weather Alerts ── */
    .weather-alert-frost {
        background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
        border-left: 5px solid var(--sky-blue);
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(2,136,209,0.12);
    }
    .weather-alert-frost strong {
        font-family: 'Merriweather', serif;
        color: #0277BD;
    }
    .weather-alert-rain {
        background: linear-gradient(135deg, #FFF3E0, #FFE0B2);
        border-left: 5px solid var(--sunrise-orange);
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(239,108,0,0.12);
    }
    .weather-alert-rain strong {
        font-family: 'Merriweather', serif;
        color: #E65100;
    }
    .weather-ok {
        background: linear-gradient(135deg, var(--field-green), #C8E6C9);
        border-left: 5px solid var(--leaf-dark);
        border-radius: 12px;
        padding: 1rem 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(46,125,50,0.1);
    }
    .weather-ok strong {
        font-family: 'Merriweather', serif;
        color: var(--leaf-dark);
    }

    /* ── Soil Input & Tool Sections ── */
    .soil-input label {
        font-weight: 600;
        color: var(--soil-dark) !important;
    }
    .tool-section-header {
        background: var(--warm-white);
        border: 2px solid #E0D5C1;
        border-radius: 16px;
        padding: 1.5rem 2rem;
        margin-bottom: 1.5rem;
        position: relative;
        overflow: hidden;
    }
    .tool-section-header::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--soil-dark), var(--leaf-dark), var(--wheat-gold));
    }
    .tool-section-header h2 {
        color: var(--soil-dark);
        margin: 0 0 0.3rem;
        font-size: 1.5rem;
    }
    .tool-section-header p {
        color: var(--soil-light);
        margin: 0;
        font-size: 0.95rem;
    }

    /* ── Primary Action Buttons ── */
    .stButton button[kind="primary"],
    button[data-testid="stBaseButton-primary"] {
        background: linear-gradient(135deg, var(--soil-dark), var(--soil-medium)) !important;
        color: var(--cream) !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        padding: 0.6rem 1.5rem !important;
        letter-spacing: 0.3px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(62,39,35,0.2) !important;
    }
    button[data-testid="stBaseButton-primary"]:hover {
        background: linear-gradient(135deg, var(--leaf-dark), var(--leaf-medium)) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(46,125,50,0.3) !important;
    }

    /* ── Quick-start buttons ── */
    .quick-start-btn button {
        background: var(--warm-white) !important;
        border: 2px solid #D7CCC8 !important;
        border-radius: 12px !important;
        color: var(--soil-dark) !important;
        font-weight: 600 !important;
        transition: all 0.3s !important;
        padding: 0.8rem !important;
    }
    .quick-start-btn button:hover {
        border-color: var(--leaf-medium) !important;
        background: var(--field-green) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(46,125,50,0.15) !important;
    }

    /* ── Stats Row ── */
    .stat-card {
        background: var(--warm-white);
        border: 1px solid #E0D5C1;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        text-align: center;
    }
    .stat-card .value {
        font-family: 'Merriweather', serif;
        font-size: 1.8rem;
        font-weight: 900;
        color: var(--soil-dark);
        line-height: 1.2;
    }
    .stat-card .label {
        font-size: 0.8rem;
        color: var(--soil-light);
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
        margin-top: 0.3rem;
    }

    /* ── Dividers ── */
    hr {
        border: none !important;
        border-top: 2px dashed #D7CCC8 !important;
        margin: 1.5rem 0 !important;
    }

    /* ── Number inputs, text areas ── */
    .stNumberInput input, .stTextArea textarea, .stTextInput input {
        border: 2px solid #D7CCC8 !important;
        border-radius: 10px !important;
        background: var(--warm-white) !important;
    }
    .stNumberInput input:focus, .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: var(--leaf-medium) !important;
        box-shadow: 0 0 0 3px rgba(67,160,71,0.15) !important;
    }

    /* ── Footer ── */
    .app-footer {
        text-align: center;
        padding: 2rem;
        color: var(--soil-light);
        font-size: 0.85rem;
        margin-top: 3rem;
        border-top: 2px dashed #D7CCC8;
    }
    .app-footer a { color: var(--leaf-dark); text-decoration: none; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# ─── Weather Functions (Open-Meteo — free, no API key) ───────

def geocode_location(place: str) -> dict | None:
    """Convert a place name to lat/lon using Open-Meteo geocoding."""
    try:
        resp = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": place, "count": 1, "language": "en"},
            timeout=5,
        )
        data = resp.json()
        if data.get("results"):
            r = data["results"][0]
            return {"lat": r["latitude"], "lon": r["longitude"], "name": r.get("name", place), "country": r.get("country", "")}
    except Exception:
        pass
    return None


def fetch_weather_forecast(lat: float, lon: float) -> dict | None:
    """Fetch 7-day hourly forecast from Open-Meteo."""
    try:
        resp = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "hourly": "temperature_2m,precipitation,wind_speed_10m,relative_humidity_2m",
                "daily": "temperature_2m_min,temperature_2m_max,precipitation_sum,wind_speed_10m_max",
                "timezone": "auto",
                "forecast_days": 7,
            },
            timeout=8,
        )
        return resp.json()
    except Exception:
        return None


def analyze_weather_alerts(forecast: dict) -> dict:
    """Parse forecast data and detect frost / heavy-rain events."""
    alerts = {"frost": [], "heavy_rain": [], "summary": []}
    daily = forecast.get("daily", {})
    dates = daily.get("time", [])
    temp_mins = daily.get("temperature_2m_min", [])
    temp_maxs = daily.get("temperature_2m_max", [])
    precip_sums = daily.get("precipitation_sum", [])
    wind_maxs = daily.get("wind_speed_10m_max", [])

    for i, date in enumerate(dates):
        t_min = temp_mins[i] if i < len(temp_mins) else None
        t_max = temp_maxs[i] if i < len(temp_maxs) else None
        rain = precip_sums[i] if i < len(precip_sums) else 0
        wind = wind_maxs[i] if i < len(wind_maxs) else 0

        day_label = datetime.strptime(date, "%Y-%m-%d").strftime("%A, %b %d")

        if t_min is not None and t_min <= 2:
            severity = "🔴 SEVERE" if t_min <= -2 else "🟡 WARNING"
            alerts["frost"].append({
                "date": day_label, "temp_min": t_min, "severity": severity
            })

        if rain >= 20:
            severity = "🔴 SEVERE" if rain >= 50 else "🟡 WARNING"
            alerts["heavy_rain"].append({
                "date": day_label, "precip_mm": rain, "wind_kmh": wind, "severity": severity
            })

        alerts["summary"].append({
            "date": day_label, "min": t_min, "max": t_max, "rain": rain, "wind": wind
        })

    return alerts


def build_weather_context(alerts: dict, location_name: str) -> str:
    """Build a context string injected into every chat message so the AI can reference live weather."""
    parts = [f"\n[LIVE WEATHER DATA for {location_name} — next 7 days]"]

    if alerts["frost"]:
        parts.append("⚠️ FROST ALERTS:")
        for f in alerts["frost"]:
            parts.append(f"  • {f['severity']} on {f['date']}: min temp {f['temp_min']}°C")

    if alerts["heavy_rain"]:
        parts.append("⚠️ HEAVY RAIN ALERTS:")
        for r in alerts["heavy_rain"]:
            parts.append(f"  • {r['severity']} on {r['date']}: {r['precip_mm']} mm rain, wind {r['wind_kmh']} km/h")

    if not alerts["frost"] and not alerts["heavy_rain"]:
        parts.append("✅ No frost or heavy-rain warnings in the next 7 days.")

    parts.append("\n7-Day Overview:")
    for s in alerts["summary"]:
        parts.append(f"  {s['date']}: {s['min']}–{s['max']}°C, rain {s['rain']} mm, wind {s['wind']} km/h")

    parts.append("\nUse this weather data to adjust irrigation scheduling, warn about frost-sensitive crops, and recommend pest/disease prevention tied to rain events.\n")
    return "\n".join(parts)


def render_weather_banner(alerts: dict, location_name: str):
    """Show a visual weather alert banner at the top of the chat."""
    frost_count = len(alerts["frost"])
    rain_count = len(alerts["heavy_rain"])

    if frost_count:
        frost_dates = ", ".join(f["date"] for f in alerts["frost"])
        st.markdown(f"""
        <div class="weather-alert-frost">
            <strong>🥶 Frost Alert — {location_name}</strong><br>
            <span>{frost_count} frost event(s) expected: {frost_dates}</span><br>
            <small>The AI will automatically factor this into irrigation & crop advice.</small>
        </div>
        """, unsafe_allow_html=True)

    if rain_count:
        rain_dates = ", ".join(f"{r['date']} ({r['precip_mm']}mm)" for r in alerts["heavy_rain"])
        st.markdown(f"""
        <div class="weather-alert-rain">
            <strong>🌧️ Heavy Rain Alert — {location_name}</strong><br>
            <span>{rain_count} heavy-rain event(s): {rain_dates}</span><br>
            <small>The AI will adjust pest management & irrigation advice accordingly.</small>
        </div>
        """, unsafe_allow_html=True)

    if not frost_count and not rain_count:
        st.markdown(f"""
        <div class="weather-ok">
            <strong>☀️ Weather looks clear — {location_name}</strong><br>
            <small>No frost or heavy-rain warnings for the next 7 days.</small>
        </div>
        """, unsafe_allow_html=True)


# ─── Language Options ────────────────────────────────────────
LANGUAGES = {
    "English": "English",
    "हिन्दी (Hindi)": "Hindi",
    "ಕನ್ನಡ (Kannada)": "Kannada",
    "தமிழ் (Tamil)": "Tamil",
    "తెలుగు (Telugu)": "Telugu",
    "मराठी (Marathi)": "Marathi",
    "বাংলা (Bengali)": "Bengali",
    "ਪੰਜਾਬੀ (Punjabi)": "Punjabi",
    "ગુજરાતી (Gujarati)": "Gujarati",
    "اردو (Urdu)": "Urdu",
    "Español (Spanish)": "Spanish",
    "Português (Portuguese)": "Portuguese",
    "Français (French)": "French",
    "Kiswahili (Swahili)": "Swahili",
    "中文 (Chinese)": "Chinese",
    "Bahasa Indonesia": "Indonesian",
}

# ─── System Prompt ───────────────────────────────────────────
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

# ─── Groq Client ─────────────────────────────────────────────
def get_client():
    api_key = st.session_state.get("groq_api_key", "")
    if not api_key:
        return None
    return Groq(api_key=api_key)


def chat(messages: list, model: str = "llama-3.3-70b-versatile") -> str:
    client = get_client()
    if not client:
        return "⚠️ Please enter your Groq API key in the sidebar."
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.6,
            max_tokens=2048,
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
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {"role": "system", "content": get_system_prompt()},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}},
                    ],
                },
            ],
            temperature=0.5,
            max_tokens=2048,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"


# ─── Session State ───────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "groq_api_key" not in st.session_state:
    st.session_state.groq_api_key = ""
if "weather_context" not in st.session_state:
    st.session_state.weather_context = ""
if "weather_alerts" not in st.session_state:
    st.session_state.weather_alerts = None
if "weather_location" not in st.session_state:
    st.session_state.weather_location = ""
if "language" not in st.session_state:
    st.session_state.language = "English"

# ─── Sidebar ─────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🌾 AgriExpert AI")
    st.caption("Your Smart Farming Companion")
    st.markdown("---")

    st.markdown("##### 🔑 API Configuration")
    api_key = st.text_input(
        "Groq API Key",
        type="password",
        value=st.session_state.groq_api_key,
        help="Get your free key at https://console.groq.com",
    )
    st.session_state.groq_api_key = api_key

    st.markdown("---")

    # ── Language Selector ──
    st.markdown("##### 🌐 Language / भाषा")
    selected_lang = st.selectbox(
        "Response Language",
        options=list(LANGUAGES.keys()),
        index=list(LANGUAGES.keys()).index(st.session_state.language),
        help="The AI will respond in this language while keeping technical terms clear",
    )
    st.session_state.language = selected_lang

    st.markdown("---")

    # ── Weather Location ──
    st.markdown("##### 🌦️ Weather Alerts")
    weather_loc = st.text_input(
        "Farm Location",
        placeholder="e.g. Pune, Delhi, Iowa, São Paulo",
        help="Enter your farm's city/region to get 7-day frost & rain alerts",
    )
    if st.button("📡 Fetch Weather", use_container_width=True):
        if weather_loc.strip():
            with st.spinner("Locating & fetching forecast..."):
                geo = geocode_location(weather_loc.strip())
                if geo:
                    forecast = fetch_weather_forecast(geo["lat"], geo["lon"])
                    if forecast:
                        loc_label = f"{geo['name']}, {geo['country']}"
                        alerts = analyze_weather_alerts(forecast)
                        st.session_state.weather_alerts = alerts
                        st.session_state.weather_location = loc_label
                        st.session_state.weather_context = build_weather_context(alerts, loc_label)
                        st.success(f"✅ Weather loaded for {loc_label}")
                    else:
                        st.error("Could not fetch forecast. Try again.")
                else:
                    st.error("Location not found. Try a different city name.")
        else:
            st.warning("Enter a location first.")

    if st.session_state.weather_location:
        st.caption(f"📍 Active: {st.session_state.weather_location}")

    st.markdown("---")
    st.markdown("##### 🧰 Tools")
    tool = st.radio(
        "Select a mode:",
        ["💬 Chat", "🧪 Soil Analysis", "📸 Leaf Diagnosis", "🌾 Crop Recommender", "🌦️ Weather Dashboard"],
        label_visibility="collapsed",
    )

    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown(
        "<div style='text-align:center; opacity:0.5; font-size:0.75rem; padding:0.5rem;'>"
        "Powered by Groq AI<br>Built with ❤️ for Farmers"
        "</div>",
        unsafe_allow_html=True,
    )

# ─── Header ──────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>🌾 AgriExpert AI</h1>
    <p>Your intelligent farming assistant — crop advice, soil analysis, pest diagnosis & weather alerts</p>
    <span class="tagline">🤖 AI-Powered Precision Agriculture</span>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# TOOL: Chat
# ═══════════════════════════════════════════════════════════════
if tool == "💬 Chat":
    # Show weather banner if available
    if st.session_state.weather_alerts:
        render_weather_banner(st.session_state.weather_alerts, st.session_state.weather_location)

    # Quick-start cards
    if not st.session_state.messages:
        st.markdown("#### 🌱 How can I help your farm today?")
        cols = st.columns(4)
        cards = [
            ("🌱", "Crop Selection", "Best crops for my region & season", "What should I plant this season?"),
            ("💧", "Irrigation", "Smart watering schedules", "How often should I water my wheat?"),
            ("🐛", "Pest Control", "Disease identification & treatment", "Yellow spots on my tomato leaves"),
            ("🌦️", "Weather Advice", "Prepare for upcoming conditions", "How should I prepare for the upcoming weather?"),
        ]
        for col, (icon, title, desc, hint) in zip(cols, cards):
            with col:
                st.markdown(f"""
                <div class="feature-card">
                    <div class="icon">{icon}</div>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"Ask about {title}", use_container_width=True, key=f"card_{title}"):
                    st.session_state.messages.append({"role": "user", "content": hint})
                    system_msg = get_system_prompt()
                    msgs = [{"role": "system", "content": system_msg}] + st.session_state.messages
                    reply = chat(msgs)
                    st.session_state.messages.append({"role": "assistant", "content": reply})
                    st.rerun()

    # Chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"], avatar="🧑‍🌾" if msg["role"] == "user" else "🌿"):
            st.markdown(msg["content"])

    # Chat input
    if prompt := st.chat_input("Ask me anything about farming... 🌾"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="🧑‍🌾"):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar="🌿"):
            with st.spinner("🌱 Analyzing your question..."):
                system_msg = get_system_prompt()
                msgs = [{"role": "system", "content": system_msg}] + st.session_state.messages
                reply = chat(msgs)
                st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})

# ═══════════════════════════════════════════════════════════════
# TOOL: Weather Dashboard
# ═══════════════════════════════════════════════════════════════
elif tool == "🌦️ Weather Dashboard":
    st.markdown("""
    <div class="tool-section-header">
        <h2>🌦️ 7-Day Weather Dashboard</h2>
        <p>Real-time weather monitoring for your farm — frost & heavy rain alerts included</p>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.weather_alerts:
        st.info("👈 Enter your farm location in the sidebar and click **Fetch Weather** to see the forecast.")
    else:
        alerts = st.session_state.weather_alerts
        loc = st.session_state.weather_location
        render_weather_banner(alerts, loc)

        # Stats row
        summary = alerts["summary"]
        if summary:
            cols = st.columns(4)
            temps_min = [s["min"] for s in summary if s["min"] is not None]
            temps_max = [s["max"] for s in summary if s["max"] is not None]
            total_rain = sum(s["rain"] for s in summary)
            max_wind = max(s["wind"] for s in summary) if summary else 0

            stats = [
                (f"{min(temps_min):.0f}°C" if temps_min else "—", "Lowest Temp"),
                (f"{max(temps_max):.0f}°C" if temps_max else "—", "Highest Temp"),
                (f"{total_rain:.0f}mm", "Total Rainfall"),
                (f"{max_wind:.0f}km/h", "Max Wind"),
            ]
            for col, (val, label) in zip(cols, stats):
                with col:
                    st.markdown(f"""
                    <div class="stat-card">
                        <div class="value">{val}</div>
                        <div class="label">{label}</div>
                    </div>
                    """, unsafe_allow_html=True)

        st.markdown("### 📅 Daily Forecast")
        for day in alerts["summary"]:
            frost_tag = " 🥶" if day["min"] is not None and day["min"] <= 2 else ""
            rain_tag = " 🌧️" if day["rain"] >= 20 else ""
            st.markdown(
                f"**{day['date']}** — "
                f"🌡️ {day['min']}°C to {day['max']}°C | "
                f"💧 {day['rain']} mm | "
                f"💨 {day['wind']} km/h"
                f"{frost_tag}{rain_tag}"
            )

        st.markdown("---")
        st.markdown("### 🤖 AI Weather Analysis")
        if st.button("Get AI interpretation of this forecast", use_container_width=True, type="primary"):
            prompt = f"""Based on the following weather forecast for {loc}, provide a comprehensive farming advisory:

{st.session_state.weather_context}

Cover:
1. **Urgent Warnings** — frost or heavy rain actions needed NOW
2. **Irrigation Adjustments** — specific schedule changes for the week
3. **Pest & Disease Risk** — what to watch for given humidity/rain
4. **Crop Protection** — steps to protect vulnerable crops
5. **Optimal Field Work Windows** — best days for spraying, planting, harvesting"""

            with st.spinner("🌱 Generating weather-aware farming advice..."):
                msgs = [{"role": "system", "content": get_system_prompt()}, {"role": "user", "content": prompt}]
                result = chat(msgs)
            st.markdown(result)

# ═══════════════════════════════════════════════════════════════
# TOOL: Soil Analysis
# ═══════════════════════════════════════════════════════════════
elif tool == "🧪 Soil Analysis":
    st.markdown("""
    <div class="tool-section-header">
        <h2>🧪 Soil Nutrient Analyzer</h2>
        <p>Enter your soil test values to get precise fertilizer recommendations & soil health insights</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        nitrogen = st.number_input("Nitrogen (N) mg/kg", 0, 500, 80)
    with col2:
        phosphorus = st.number_input("Phosphorus (P) mg/kg", 0, 500, 40)
    with col3:
        potassium = st.number_input("Potassium (K) mg/kg", 0, 500, 60)
    with col4:
        ph = st.number_input("Soil pH", 0.0, 14.0, 6.5, step=0.1)

    col5, col6 = st.columns(2)
    with col5:
        soil_type = st.selectbox("Soil Type", ["Loamy", "Sandy", "Clay", "Silty", "Peaty", "Chalky"])
    with col6:
        crop = st.text_input("Target Crop (optional)", placeholder="e.g. Rice, Wheat, Tomato")

    if st.button("🔬 Analyze Soil", use_container_width=True, type="primary"):
        weather_note = ""
        if st.session_state.weather_context:
            weather_note = f"\n\nAlso consider this upcoming weather when making recommendations:\n{st.session_state.weather_context}"

        prompt = f"""Analyze this soil report and give detailed fertilizer recommendations:
- Nitrogen (N): {nitrogen} mg/kg
- Phosphorus (P): {phosphorus} mg/kg
- Potassium (K): {potassium} mg/kg
- Soil pH: {ph}
- Soil Type: {soil_type}
- Target Crop: {crop if crop else 'Not specified — suggest suitable crops'}
{weather_note}

Provide:
1. Assessment of each nutrient level (low/medium/high)
2. Specific fertilizer recommendations with dosage
3. Soil amendments needed
4. Suitable crops for this soil profile
5. Long-term soil health improvement plan"""

        with st.spinner("🧪 Analyzing soil data..."):
            msgs = [{"role": "system", "content": get_system_prompt()}, {"role": "user", "content": prompt}]
            result = chat(msgs)
        st.markdown("---")
        st.markdown(result)

# ═══════════════════════════════════════════════════════════════
# TOOL: Leaf Diagnosis (Image Upload)
# ═══════════════════════════════════════════════════════════════
elif tool == "📸 Leaf Diagnosis":
    st.markdown("""
    <div class="tool-section-header">
        <h2>📸 Leaf & Crop Disease Diagnosis</h2>
        <p>Upload a photo of a sick plant for instant AI-powered diagnosis and treatment plan</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded = st.file_uploader("Upload leaf/crop image", type=["jpg", "jpeg", "png", "webp"])
    symptoms = st.text_area("Describe symptoms (optional)", placeholder="e.g. yellow spots, curling, holes, wilting...")

    if uploaded:
        st.image(uploaded, caption="📷 Uploaded Image", width=400)

        if st.button("🔍 Diagnose", use_container_width=True, type="primary"):
            weather_note = ""
            if st.session_state.weather_context:
                weather_note = f"\n\nCurrent weather context (may be relevant to the diagnosis):\n{st.session_state.weather_context}"

            prompt = f"""You are an expert plant pathologist. Analyze this image of a crop/leaf.
{f'The farmer describes these symptoms: {symptoms}' if symptoms else ''}
{weather_note}

Provide:
1. **Identified Disease/Pest** — name and brief description
2. **Confidence Level** — how certain you are
3. **Organic Treatment** — natural remedies
4. **Chemical Treatment** — specific active ingredients and products
5. **Prevention** — steps to avoid recurrence
⚠️ Always remind to follow local regulations for pesticide use."""

            with st.spinner("🔬 Analyzing image..."):
                result = analyze_image(uploaded.read(), prompt)
            st.markdown("---")
            st.markdown(result)

# ═══════════════════════════════════════════════════════════════
# TOOL: Crop Recommender
# ═══════════════════════════════════════════════════════════════
elif tool == "🌾 Crop Recommender":
    st.markdown("""
    <div class="tool-section-header">
        <h2>🌾 Smart Crop Recommender</h2>
        <p>Get personalized crop suggestions based on your location, climate, and farm conditions</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        location = st.text_input("Location / Region", placeholder="e.g. Punjab, Maharashtra, Iowa")
        season = st.selectbox("Season", ["Kharif (Monsoon/Summer)", "Rabi (Winter)", "Zaid (Spring/Summer)", "Year-round"])
    with col2:
        avg_temp = st.slider("Avg Temperature (°C)", 5, 50, 28)
        rainfall = st.slider("Annual Rainfall (mm)", 100, 3000, 800)

    water_avail = st.selectbox("Water Availability", ["Rain-fed only", "Limited irrigation", "Full irrigation available"])
    farm_size = st.selectbox("Farm Size", ["Small (< 2 acres)", "Medium (2-10 acres)", "Large (> 10 acres)"])

    if st.button("🌱 Get Recommendations", use_container_width=True, type="primary"):
        weather_note = ""
        if st.session_state.weather_context:
            weather_note = f"\n\nUpcoming weather forecast to factor in:\n{st.session_state.weather_context}"

        prompt = f"""Recommend the best crops for this farmer:
- Location: {location}
- Season: {season}
- Average Temperature: {avg_temp}°C
- Annual Rainfall: {rainfall} mm
- Water Availability: {water_avail}
- Farm Size: {farm_size}
{weather_note}

Provide:
1. **Top 5 recommended crops** with reasons
2. **Expected yield** per acre
3. **Estimated cost & profit** analysis
4. **Crop rotation** plan for soil health
5. **Risk factors** to watch for"""

        with st.spinner("🌾 Computing recommendations..."):
            msgs = [{"role": "system", "content": get_system_prompt()}, {"role": "user", "content": prompt}]
            result = chat(msgs)
        st.markdown("---")
        st.markdown(result)

# ─── Footer ──────────────────────────────────────────────────
st.markdown("""
<div class="app-footer">
    🌾 <strong>AgriExpert AI</strong> — Empowering farmers with intelligent, data-driven agriculture<br>
    Built with <a href="https://streamlit.io" target="_blank">Streamlit</a> & <a href="https://groq.com" target="_blank">Groq AI</a>
</div>
""", unsafe_allow_html=True)
