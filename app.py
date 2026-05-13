"""
AgriExpert AI — Smart Farming Assistant
Built with Streamlit + Groq AI
Includes real-time weather alerts (frost & heavy rain) via Open-Meteo API

This is the refactored version with modular architecture:
- config.py: Configuration and constants
- styles.py: CSS styling
- weather_service.py: Weather API functions
- groq_service.py: AI chat and vision functions
- ui_components.py: Reusable UI components
"""

import streamlit as st
from config import APP_CONFIG, SESSION_DEFAULTS, TOOL_OPTIONS, LANGUAGES
from styles import get_css_styles
from weather_service import geocode_location, fetch_weather_forecast, analyze_weather_alerts, build_weather_context
from groq_service import chat, analyze_image, get_system_prompt
from ui_components import (
    render_main_header,
    render_feature_cards,
    render_weather_banner,
    render_tool_section_header,
    render_stat_card,
    render_chat_message,
    render_footer,
)


# ─── Page Config ─────────────────────────────────────────────
st.set_page_config(
    page_title=APP_CONFIG["page_title"],
    page_icon=APP_CONFIG["page_icon"],
    layout=APP_CONFIG["layout"],
    initial_sidebar_state=APP_CONFIG["initial_sidebar_state"],
)

# ─── Custom CSS ──────────────────────────────────────────────
st.markdown(get_css_styles(), unsafe_allow_html=True)

# ─── Session State Initialization ────────────────────────────
for key, default_value in SESSION_DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = default_value


# ─── Sidebar ─────────────────────────────────────────────────
def render_sidebar() -> str:
    """Render the sidebar and return the selected tool."""
    with st.sidebar:
        st.markdown("## 🌾 AgriExpert AI")
        st.caption("Your Smart Farming Companion")
        st.markdown("---")

        # API Configuration
        st.markdown("##### 🔑 API Configuration")
        api_key = st.text_input(
            "Groq API Key",
            type="password",
            value=st.session_state.groq_api_key,
            help="Get your free key at https://console.groq.com",
        )
        st.session_state.groq_api_key = api_key

        st.markdown("---")

        # Language Selector
        st.markdown("##### 🌐 Language / भाषा")
        selected_lang = st.selectbox(
            "Response Language",
            options=list(LANGUAGES.keys()),
            index=list(LANGUAGES.keys()).index(st.session_state.language),
            help="The AI will respond in this language while keeping technical terms clear",
        )
        st.session_state.language = selected_lang

        st.markdown("---")

        # Weather Location
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

        # Tools
        st.markdown("##### 🧰 Tools")
        tool = st.radio(
            "Select a mode:",
            TOOL_OPTIONS,
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

        return tool


# ─── Tool: Chat ──────────────────────────────────────────────
def render_chat_tool():
    """Render the main chat interface."""
    # Show weather banner if available
    if st.session_state.weather_alerts:
        render_weather_banner(st.session_state.weather_alerts, st.session_state.weather_location)

    # Quick-start cards if no messages
    if not st.session_state.messages:
        hint = render_feature_cards()
        if hint:
            st.session_state.messages.append({"role": "user", "content": hint})
            system_msg = get_system_prompt()
            msgs = [{"role": "system", "content": system_msg}] + st.session_state.messages
            reply = chat(msgs)
            st.session_state.messages.append({"role": "assistant", "content": reply})
            st.rerun()

    # Chat history
    for msg in st.session_state.messages:
        render_chat_message(msg["role"], msg["content"])

    # Chat input
    if prompt := st.chat_input("Ask me anything about farming... 🌾"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        render_chat_message("user", prompt)

        with st.chat_message("assistant", avatar="🌿"):
            with st.spinner("🌱 Analyzing your question..."):
                system_msg = get_system_prompt()
                msgs = [{"role": "system", "content": system_msg}] + st.session_state.messages
                reply = chat(msgs)
                st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})


# ─── Tool: Weather Dashboard ─────────────────────────────────
def render_weather_dashboard():
    """Render the weather dashboard tool."""
    render_tool_section_header(
        "🌦️ 7-Day Weather Dashboard",
        "Real-time weather monitoring for your farm — frost & heavy rain alerts included",
    )

    if not st.session_state.weather_alerts:
        st.info("👈 Enter your farm location in the sidebar and click **Fetch Weather** to see the forecast.")
        return

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
                st.markdown(render_stat_card(val, label), unsafe_allow_html=True)

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


# ─── Tool: Soil Analysis ─────────────────────────────────────
def render_soil_analysis():
    """Render the soil analysis tool."""
    render_tool_section_header(
        "🧪 Soil Nutrient Analyzer",
        "Enter your soil test values to get precise fertilizer recommendations & soil health insights",
    )

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


# ─── Tool: Leaf Diagnosis ────────────────────────────────────
def render_leaf_diagnosis():
    """Render the leaf diagnosis tool."""
    render_tool_section_header(
        "📸 Leaf & Crop Disease Diagnosis",
        "Upload a photo of a sick plant for instant AI-powered diagnosis and treatment plan",
    )

    uploaded = st.file_uploader("Upload leaf/crop image", type=["jpg", "jpeg", "png", "webp"])
    symptoms = st.text_area(
        "Describe symptoms (optional)",
        placeholder="e.g. yellow spots, curling, holes, wilting...",
    )

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


# ─── Tool: Crop Recommender ──────────────────────────────────
def render_crop_recommender():
    """Render the crop recommender tool."""
    render_tool_section_header(
        "🌾 Smart Crop Recommender",
        "Get personalized crop suggestions based on your location, climate, and farm conditions",
    )

    col1, col2 = st.columns(2)
    with col1:
        location = st.text_input("Location / Region", placeholder="e.g. Punjab, Maharashtra, Iowa")
        season = st.selectbox(
            "Season",
            ["Kharif (Monsoon/Summer)", "Rabi (Winter)", "Zaid (Spring/Summer)", "Year-round"],
        )
    with col2:
        avg_temp = st.slider("Avg Temperature (°C)", 5, 50, 28)
        rainfall = st.slider("Annual Rainfall (mm)", 100, 3000, 800)

    water_avail = st.selectbox(
        "Water Availability",
        ["Rain-fed only", "Limited irrigation", "Full irrigation available"],
    )
    farm_size = st.selectbox(
        "Farm Size",
        ["Small (< 2 acres)", "Medium (2-10 acres)", "Large (> 10 acres)"],
    )

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


# ═══════════════════════════════════════════════════════════════
# MAIN APP
# ═══════════════════════════════════════════════════════════════

def main():
    """Main application entry point."""
    # Render sidebar and get selected tool
    tool = render_sidebar()

    # Render main header
    render_main_header()

    # Route to selected tool
    tool_handlers = {
        "💬 Chat": render_chat_tool,
        "🌦️ Weather Dashboard": render_weather_dashboard,
        "🧪 Soil Analysis": render_soil_analysis,
        "📸 Leaf Diagnosis": render_leaf_diagnosis,
        "🌾 Crop Recommender": render_crop_recommender,
    }

    handler = tool_handlers.get(tool, render_chat_tool)
    handler()

    # Render footer
    render_footer()


if __name__ == "__main__":
    main()
