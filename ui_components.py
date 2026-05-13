"""
UI Components for AgriExpert AI Streamlit App
"""

import streamlit as st
from config import COLORS, QUICK_START_CARDS


def render_main_header():
    """Render the main app header with animated elements."""
    st.markdown(
        """
<div class="main-header">
    <h1>🌾 AgriExpert AI</h1>
    <p>Your intelligent farming assistant — crop advice, soil analysis, pest diagnosis & weather alerts</p>
    <span class="tagline">🤖 AI-Powered Precision Agriculture</span>
</div>
""",
        unsafe_allow_html=True,
    )


def render_feature_cards():
    """Render quick-start feature cards with enhanced interactivity and handle button clicks."""
    st.markdown("#### 🌱 How can I help your farm today?")
    cols = st.columns(4)

    for col, (icon, title, desc, hint) in zip(cols, QUICK_START_CARDS):
        with col:
            # Add hover effect container
            st.markdown(
                f"""
                <div class="feature-card" data-tooltip="{desc}">
                    <div class="icon">{icon}</div>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button(f"Ask about {title}", use_container_width=True, key=f"card_{title}", type="secondary"):
                return hint
    return None


def render_weather_banner(alerts: dict, location_name: str):
    """Show a visual weather alert banner at the top of the chat with animated icons."""
    frost_count = len(alerts["frost"])
    rain_count = len(alerts["heavy_rain"])

    if frost_count:
        frost_dates = ", ".join(f["date"] for f in alerts["frost"])
        st.markdown(
            f"""
        <div class="weather-alert-frost">
            <strong>🥶 Frost Alert — {location_name}</strong><br>
            <span>{frost_count} frost event(s) expected: {frost_dates}</span><br>
            <small>The AI will automatically factor this into irrigation & crop advice.</small>
        </div>
        """,
            unsafe_allow_html=True,
        )

    if rain_count:
        rain_dates = ", ".join(
            f"{r['date']} ({r['precip_mm']}mm)" for r in alerts["heavy_rain"]
        )
        st.markdown(
            f"""
        <div class="weather-alert-rain">
            <strong>🌧️ Heavy Rain Alert — {location_name}</strong><br>
            <span>{rain_count} heavy-rain event(s): {rain_dates}</span><br>
            <small>The AI will adjust pest management & irrigation advice accordingly.</small>
        </div>
        """,
            unsafe_allow_html=True,
        )

    if not frost_count and not rain_count:
        st.markdown(
            f"""
        <div class="weather-ok">
            <strong>☀️ Weather looks clear — {location_name}</strong><br>
            <small>No frost or heavy-rain warnings for the next 7 days.</small>
        </div>
        """,
            unsafe_allow_html=True,
        )


def render_tool_section_header(title: str, description: str):
    """Render a tool section header with animated gradient border."""
    st.markdown(
        f"""
    <div class="tool-section-header">
        <h2>{title}</h2>
        <p>{description}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_stat_card(value: str, label: str) -> str:
    """Return HTML for a stat card with hover animation."""
    return f"""
    <div class="stat-card">
        <div class="value">{value}</div>
        <div class="label">{label}</div>
    </div>
    """


def render_chat_message(role: str, content: str):
    """Render a single chat message with animated avatar."""
    avatar = "🧑‍🌾" if role == "user" else "🌿"
    with st.chat_message(role, avatar=avatar):
        st.markdown(content)


def render_footer():
    """Render the app footer with animated hover links."""
    st.markdown(
        """
<div class="app-footer">
    🌾 <strong>AgriExpert AI</strong> — Empowering farmers with intelligent, data-driven agriculture<br>
    Built with <a href="https://streamlit.io" target="_blank">Streamlit</a> & <a href="https://groq.com" target="_blank">Groq AI</a>
</div>
""",
        unsafe_allow_html=True,
    )
