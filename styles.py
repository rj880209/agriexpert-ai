"""
CSS Styles for AgriExpert AI Streamlit App
Enhanced with animations, interactive elements, and modern UI effects
"""

from config import COLORS


def get_css_styles() -> str:
    """Return the complete CSS stylesheet for the app with enhanced interactivity."""
    return f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Source+Sans+3:wght@400;500;600;700&display=swap');

    /* ═══════════════════════════════════════════════════════════
       GLOBAL & ANIMATIONS
       ═══════════════════════════════════════════════════════════ */
    * {{ font-family: 'Source Sans 3', sans-serif; }}
    h1, h2, h3, h4, h5, h6 {{ font-family: 'Merriweather', serif !important; }}

    /* Smooth scrolling */
    html {{ scroll-behavior: smooth; }}

    /* Keyframe Animations */
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    
    @keyframes slideInLeft {{
        from {{ opacity: 0; transform: translateX(-20px); }}
        to {{ opacity: 1; transform: translateX(0); }}
    }}
    
    @keyframes slideInRight {{
        from {{ opacity: 0; transform: translateX(20px); }}
        to {{ opacity: 1; transform: translateX(0); }}
    }}
    
    @keyframes pulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.05); }}
    }}
    
    @keyframes shimmer {{
        0% {{ background-position: -1000px 0; }}
        100% {{ background-position: 1000px 0; }}
    }}
    
    @keyframes bounce {{
        0%, 20%, 50%, 80%, 100% {{ transform: translateY(0); }}
        40% {{ transform: translateY(-8px); }}
        60% {{ transform: translateY(-4px); }}
    }}
    
    @keyframes leafFloat {{
        0%, 100% {{ transform: translateY(0) rotate(0deg); }}
        50% {{ transform: translateY(-5px) rotate(5deg); }}
    }}

    .stApp {{
        background: linear-gradient(180deg, {COLORS['warm_white']} 0%, {COLORS['parchment']} 40%, #E8E0D0 100%);
    }}
    
    /* Fade in all main content */
    div[data-testid="stMain"] > * {{
        animation: fadeIn 0.5s ease-out;
    }}

    /* ═══════════════════════════════════════════════════════════
       SIDEBAR ENHANCEMENTS
       ═══════════════════════════════════════════════════════════ */
    div[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {COLORS['soil_dark']} 0%, {COLORS['soil_medium']} 100%) !important;
        border-right: 3px solid {COLORS['wheat_gold']};
        box-shadow: 4px 0 20px rgba(0,0,0,0.15);
    }}
    div[data-testid="stSidebar"] * {{
        color: {COLORS['cream']} !important;
    }}
    div[data-testid="stSidebar"] .stSelectbox label,
    div[data-testid="stSidebar"] .stTextInput label {{
        color: {COLORS['wheat_light']} !important;
        font-weight: 600 !important;
    }}
    div[data-testid="stSidebar"] .stRadio label {{
        color: {COLORS['cream']} !important;
        font-size: 0.95rem !important;
        padding: 0.5rem 0 !important;
        transition: all 0.3s !important;
    }}
    div[data-testid="stSidebar"] .stRadio label:hover {{
        color: {COLORS['wheat_light']} !important;
        padding-left: 8px !important;
    }}
    div[data-testid="stSidebar"] input,
    div[data-testid="stSidebar"] select {{
        background: rgba(255,255,255,0.1) !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        color: white !important;
        border-radius: 8px !important;
        transition: all 0.3s !important;
    }}
    div[data-testid="stSidebar"] input:focus,
    div[data-testid="stSidebar"] select:focus {{
        background: rgba(255,255,255,0.15) !important;
        border-color: {COLORS['wheat_light']} !important;
        box-shadow: 0 0 0 2px rgba(249,168,37,0.3) !important;
    }}
    div[data-testid="stSidebar"] .stButton button {{
        background: linear-gradient(135deg, {COLORS['leaf_dark']}, {COLORS['leaf_medium']}) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: all 0.3s !important;
        position: relative;
        overflow: hidden;
    }}
    div[data-testid="stSidebar"] .stButton button::before {{
        content: '';
        position: absolute;
        top: 0; left: -100%;
        width: 100%; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }}
    div[data-testid="stSidebar"] .stButton button:hover::before {{
        left: 100%;
    }}
    div[data-testid="stSidebar"] .stButton button:hover {{
        background: linear-gradient(135deg, {COLORS['leaf_medium']}, {COLORS['leaf_light']}) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(46,125,50,0.4) !important;
    }}
    div[data-testid="stSidebar"] hr {{
        border-color: rgba(255,255,255,0.15) !important;
    }}
    
    /* Sidebar header with icon animation */
    div[data-testid="stSidebar"] .main-header-sidebar {{
        text-align: center;
        padding: 1rem 0;
        margin-bottom: 1rem;
    }}
    div[data-testid="stSidebar"] .sidebar-icon {{
        font-size: 3rem;
        display: inline-block;
        animation: leafFloat 3s ease-in-out infinite;
    }}

    /* ═══════════════════════════════════════════════════════════
       MAIN HEADER WITH PARALLAX EFFECT
       ═══════════════════════════════════════════════════════════ */
    .main-header {{
        background: linear-gradient(135deg, {COLORS['soil_dark']} 0%, {COLORS['soil_medium']} 40%, {COLORS['leaf_dark']} 100%);
        padding: 2.5rem 3rem;
        border-radius: 20px;
        color: white;
        margin-bottom: 1.5rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(62,39,35,0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    .main-header:hover {{
        transform: translateY(-3px);
        box-shadow: 0 12px 40px rgba(62,39,35,0.4);
    }}
    .main-header::before {{
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, rgba(249,168,37,0.15) 0%, transparent 70%);
        border-radius: 50%;
        animation: pulse 4s ease-in-out infinite;
    }}
    .main-header::after {{
        content: '🌾🌱🌿';
        position: absolute;
        bottom: 10px;
        right: 20px;
        font-size: 2rem;
        opacity: 0.2;
        letter-spacing: 8px;
        animation: leafFloat 5s ease-in-out infinite;
    }}
    .main-header h1 {{
        margin: 0;
        font-size: 2.4rem;
        font-weight: 900;
        font-family: 'Merriweather', serif !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        letter-spacing: -0.5px;
        animation: slideInLeft 0.6s ease-out;
    }}
    .main-header p {{
        margin: 0.5rem 0 0;
        opacity: 0.9;
        font-size: 1.1rem;
        font-weight: 400;
        letter-spacing: 0.3px;
        animation: slideInLeft 0.7s ease-out;
    }}
    .main-header .tagline {{
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
        animation: slideInRight 0.8s ease-out;
        transition: all 0.3s;
    }}
    .main-header .tagline:hover {{
        background: rgba(249,168,37,0.35);
        transform: scale(1.05);
    }}

    /* ═══════════════════════════════════════════════════════════
       FEATURE CARDS WITH HOVER EFFECTS
       ═══════════════════════════════════════════════════════════ */
    .feature-card {{
        background: {COLORS['warm_white']};
        border: 2px solid #E0D5C1;
        border-radius: 16px;
        padding: 1.5rem 1.2rem;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 2px 8px rgba(93,64,55,0.08);
        position: relative;
        overflow: hidden;
        cursor: pointer;
    }}
    .feature-card::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 4px;
        background: linear-gradient(90deg, {COLORS['leaf_dark']}, {COLORS['wheat_gold']});
        transform: scaleX(0);
        transition: transform 0.4s ease;
    }}
    .feature-card:hover::before {{
        transform: scaleX(1);
    }}
    .feature-card:hover {{
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 12px 32px rgba(93,64,55,0.2);
        border-color: {COLORS['leaf_medium']};
    }}
    .feature-card .icon {{ 
        font-size: 2.5rem; 
        margin-bottom: 0.8rem;
        display: inline-block;
        transition: transform 0.3s;
    }}
    .feature-card:hover .icon {{
        transform: scale(1.2) rotate(5deg);
        animation: bounce 0.6s;
    }}
    .feature-card h4 {{
        margin: 0;
        color: {COLORS['soil_dark']};
        font-family: 'Merriweather', serif !important;
        font-size: 1rem;
        font-weight: 700;
    }}
    .feature-card p {{
        margin: 0.4rem 0 0;
        font-size: 0.82rem;
        color: {COLORS['soil_light']};
        line-height: 1.4;
    }}

    /* ═══════════════════════════════════════════════════════════
       CHAT BUBBLES WITH ANIMATION
       ═══════════════════════════════════════════════════════════ */
    div[data-testid="stChatMessage"] {{
        border-radius: 16px !important;
        margin-bottom: 0.8rem !important;
        animation: fadeIn 0.4s ease-out;
    }}
    .chat-user {{
        background: linear-gradient(135deg, #FFF8E1, #FFF3CD);
        border: 1px solid #E0D5C1;
        border-radius: 16px 16px 4px 16px;
        padding: 1rem 1.2rem;
        margin: 0.5rem 0;
        max-width: 80%;
        margin-left: auto;
        position: relative;
    }}
    .chat-user::after {{
        content: '🧑‍🌾';
        position: absolute;
        bottom: -10px;
        right: 10px;
        font-size: 1.2rem;
    }}
    .chat-assistant {{
        background: {COLORS['warm_white']};
        border: 1px solid #D7CCC8;
        border-left: 4px solid {COLORS['leaf_dark']};
        border-radius: 16px 16px 16px 4px;
        padding: 1rem 1.2rem;
        margin: 0.5rem 0;
        max-width: 85%;
        position: relative;
    }}
    .chat-assistant::after {{
        content: '🌿';
        position: absolute;
        bottom: -10px;
        left: 10px;
        font-size: 1.2rem;
    }}

    /* ═══════════════════════════════════════════════════════════
       WEATHER ALERTS WITH PULSE ANIMATION
       ═══════════════════════════════════════════════════════════ */
    .weather-alert-frost {{
        background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
        border-left: 5px solid {COLORS['sky_blue']};
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(2,136,209,0.12);
        animation: slideInLeft 0.5s ease-out;
        position: relative;
        overflow: hidden;
    }}
    .weather-alert-frost::before {{
        content: '❄️';
        position: absolute;
        top: 10px;
        right: 15px;
        font-size: 2rem;
        opacity: 0.3;
        animation: leafFloat 2s ease-in-out infinite;
    }}
    .weather-alert-frost strong {{
        font-family: 'Merriweather', serif;
        color: #0277BD;
    }}
    .weather-alert-rain {{
        background: linear-gradient(135deg, #FFF3E0, #FFE0B2);
        border-left: 5px solid {COLORS['sunrise_orange']};
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(239,108,0,0.12);
        animation: slideInRight 0.5s ease-out;
        position: relative;
        overflow: hidden;
    }}
    .weather-alert-rain::before {{
        content: '🌧️';
        position: absolute;
        top: 10px;
        right: 15px;
        font-size: 2rem;
        opacity: 0.3;
        animation: bounce 2s ease-in-out infinite;
    }}
    .weather-alert-rain strong {{
        font-family: 'Merriweather', serif;
        color: #E65100;
    }}
    .weather-ok {{
        background: linear-gradient(135deg, {COLORS['field_green']}, #C8E6C9);
        border-left: 5px solid {COLORS['leaf_dark']};
        border-radius: 12px;
        padding: 1rem 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(46,125,50,0.1);
        animation: fadeIn 0.5s ease-out;
    }}
    .weather-ok strong {{
        font-family: 'Merriweather', serif;
        color: {COLORS['leaf_dark']};
    }}

    /* ═══════════════════════════════════════════════════════════
       TOOL SECTIONS WITH GRADIENT BORDERS
       ═══════════════════════════════════════════════════════════ */
    .tool-section-header {{
        background: {COLORS['warm_white']};
        border: 2px solid #E0D5C1;
        border-radius: 16px;
        padding: 1.5rem 2rem;
        margin-bottom: 1.5rem;
        position: relative;
        overflow: hidden;
        transition: all 0.3s;
    }}
    .tool-section-header:hover {{
        box-shadow: 0 8px 24px rgba(93,64,55,0.12);
        transform: translateY(-2px);
    }}
    .tool-section-header::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 4px;
        background: linear-gradient(90deg, {COLORS['soil_dark']}, {COLORS['leaf_dark']}, {COLORS['wheat_gold']});
        background-size: 200% 100%;
        animation: shimmer 3s linear infinite;
    }}
    .tool-section-header h2 {{
        color: {COLORS['soil_dark']};
        margin: 0 0 0.3rem;
        font-size: 1.5rem;
    }}
    .tool-section-header p {{
        color: {COLORS['soil_light']};
        margin: 0;
        font-size: 0.95rem;
    }}

    /* ═══════════════════════════════════════════════════════════
       PRIMARY ACTION BUTTONS WITH RIPPLE EFFECT
       ═══════════════════════════════════════════════════════════ */
    .stButton button[kind="primary"],
    button[data-testid="stBaseButton-primary"] {{
        background: linear-gradient(135deg, {COLORS['soil_dark']}, {COLORS['soil_medium']}) !important;
        color: {COLORS['cream']} !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        padding: 0.6rem 1.5rem !important;
        letter-spacing: 0.3px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(62,39,35,0.2) !important;
        position: relative;
        overflow: hidden;
    }}
    button[data-testid="stBaseButton-primary"]::before {{
        content: '';
        position: absolute;
        top: 50%; left: 50%;
        width: 0; height: 0;
        border-radius: 50%;
        background: rgba(255,255,255,0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }}
    button[data-testid="stBaseButton-primary"]:hover::before {{
        width: 300px; height: 300px;
    }}
    button[data-testid="stBaseButton-primary"]:hover {{
        background: linear-gradient(135deg, {COLORS['leaf_dark']}, {COLORS['leaf_medium']}) !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 24px rgba(46,125,50,0.35) !important;
    }}
    button[data-testid="stBaseButton-primary"]:active {{
        transform: translateY(-1px) !important;
    }}

    /* ═══════════════════════════════════════════════════════════
       QUICK-START BUTTONS
       ═══════════════════════════════════════════════════════════ */
    .quick-start-btn button {{
        background: {COLORS['warm_white']} !important;
        border: 2px solid #D7CCC8 !important;
        border-radius: 12px !important;
        color: {COLORS['soil_dark']} !important;
        font-weight: 600 !important;
        transition: all 0.3s !important;
        padding: 0.8rem !important;
        position: relative;
        overflow: hidden;
    }}
    .quick-start-btn button::after {{
        content: '';
        position: absolute;
        bottom: 0; left: 0;
        width: 0; height: 3px;
        background: linear-gradient(90deg, {COLORS['leaf_dark']}, {COLORS['wheat_gold']});
        transition: width 0.3s;
    }}
    .quick-start-btn button:hover::after {{
        width: 100%;
    }}
    .quick-start-btn button:hover {{
        border-color: {COLORS['leaf_medium']} !important;
        background: {COLORS['field_green']} !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 16px rgba(46,125,50,0.2) !important;
    }}

    /* ═══════════════════════════════════════════════════════════
       STATS CARDS WITH SCALE ANIMATION
       ═══════════════════════════════════════════════════════════ */
    .stat-card {{
        background: {COLORS['warm_white']};
        border: 1px solid #E0D5C1;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        text-align: center;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }}
    .stat-card::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(135deg, rgba(67,160,71,0.05), transparent);
        opacity: 0;
        transition: opacity 0.3s;
    }}
    .stat-card:hover {{
        transform: scale(1.08) translateY(-5px);
        box-shadow: 0 8px 24px rgba(93,64,55,0.15);
        border-color: {COLORS['leaf_medium']};
    }}
    .stat-card:hover::before {{
        opacity: 1;
    }}
    .stat-card .value {{
        font-family: 'Merriweather', serif;
        font-size: 1.8rem;
        font-weight: 900;
        color: {COLORS['soil_dark']};
        line-height: 1.2;
        position: relative;
    }}
    .stat-card .label {{
        font-size: 0.8rem;
        color: {COLORS['soil_light']};
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
        margin-top: 0.3rem;
        position: relative;
    }}

    /* ═══════════════════════════════════════════════════════════
       LOADING SPINNER ENHANCEMENT
       ═══════════════════════════════════════════════════════════ */
    .stSpinner > div {{
        border-top-color: {COLORS['leaf_dark']} !important;
        border-width: 3px !important;
    }}

    /* ═══════════════════════════════════════════════════════════
       DIVIDERS WITH DASHED STYLE
       ═══════════════════════════════════════════════════════════ */
    hr {{
        border: none !important;
        border-top: 2px dashed #D7CCC8 !important;
        margin: 1.5rem 0 !important;
        transition: border-color 0.3s;
    }}
    hr:hover {{
        border-color: {COLORS['leaf_medium']} !important;
    }}

    /* ═══════════════════════════════════════════════════════════
       INPUT FIELDS WITH FOCUS EFFECTS
       ═══════════════════════════════════════════════════════════ */
    .stNumberInput input, .stTextArea textarea, .stTextInput input {{
        border: 2px solid #D7CCC8 !important;
        border-radius: 10px !important;
        background: {COLORS['warm_white']} !important;
        transition: all 0.3s !important;
    }}
    .stNumberInput input:focus, .stTextArea textarea:focus, .stTextInput input:focus {{
        border-color: {COLORS['leaf_medium']} !important;
        box-shadow: 0 0 0 3px rgba(67,160,71,0.15) !important;
        transform: translateY(-1px);
    }}
    
    /* Placeholder styling */
    ::placeholder {{
        color: #A1887F !important;
        opacity: 0.7;
    }}

    /* ═══════════════════════════════════════════════════════════
       FOOTER WITH HOVER LINKS
       ═══════════════════════════════════════════════════════════ */
    .app-footer {{
        text-align: center;
        padding: 2rem;
        color: {COLORS['soil_light']};
        font-size: 0.85rem;
        margin-top: 3rem;
        border-top: 2px dashed #D7CCC8;
        background: linear-gradient(180deg, transparent, rgba(249,168,37,0.05));
        border-radius: 12px 12px 0 0;
    }}
    .app-footer a {{ 
        color: {COLORS['leaf_dark']}; 
        text-decoration: none; 
        font-weight: 600;
        transition: all 0.3s;
        position: relative;
    }}
    .app-footer a::after {{
        content: '';
        position: absolute;
        bottom: -2px; left: 0;
        width: 0; height: 2px;
        background: {COLORS['wheat_gold']};
        transition: width 0.3s;
    }}
    .app-footer a:hover::after {{
        width: 100%;
    }}
    .app-footer a:hover {{
        color: {COLORS['wheat_gold']};
    }}
    
    /* ═══════════════════════════════════════════════════════════
       TOOLTIPS (for future use)
       ═══════════════════════════════════════════════════════════ */
    [data-tooltip] {{
        position: relative;
    }}
    [data-tooltip]:hover::after {{
        content: attr(data-tooltip);
        position: absolute;
        bottom: 100%;
        left: 50%;
        transform: translateX(-50%);
        background: {COLORS['soil_dark']};
        color: white;
        padding: 0.5rem 0.8rem;
        border-radius: 6px;
        font-size: 0.75rem;
        white-space: nowrap;
        z-index: 1000;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }}
    
    /* ═══════════════════════════════════════════════════════════
       SUCCESS/ERROR MESSAGE STYLING
       ═══════════════════════════════════════════════════════════ */
    .stAlert {{
        border-radius: 12px !important;
        animation: fadeIn 0.4s ease-out;
    }}
    
    /* Image upload area enhancement */
    .stFileUploader {{
        border: 2px dashed #D7CCC8 !important;
        border-radius: 12px !important;
        transition: all 0.3s !important;
    }}
    .stFileUploader:hover {{
        border-color: {COLORS['leaf_medium']} !important;
        background: rgba(67,160,71,0.05) !important;
    }}

    /* ═══════════════════════════════════════════════════════════
       CUSTOM SCROLLBAR - PREMIUM LOOK
       ═══════════════════════════════════════════════════════════ */
    ::-webkit-scrollbar {{
        width: 10px;
        height: 10px;
    }}
    ::-webkit-scrollbar-track {{
        background: {COLORS['parchment']};
        border-radius: 10px;
    }}
    ::-webkit-scrollbar-thumb {{
        background: linear-gradient(180deg, {COLORS['soil_medium']}, {COLORS['leaf_medium']});
        border-radius: 10px;
        border: 2px solid {COLORS['parchment']};
    }}
    ::-webkit-scrollbar-thumb:hover {{
        background: linear-gradient(180deg, {COLORS['soil_dark']}, {COLORS['leaf_dark']});
    }}

    /* Firefox scrollbar */
    * {{
        scrollbar-width: thin;
        scrollbar-color: {COLORS['leaf_medium']} {COLORS['parchment']};
    }}

    /* ═══════════════════════════════════════════════════════════
       LOADING SPINNER ENHANCEMENT
       ═══════════════════════════════════════════════════════════ */
    div[data-testid="stSpinner"] {{
        color: {COLORS['leaf_dark']} !important;
    }}
    div[data-testid="stSpinner"] svg {{
        filter: drop-shadow(0 2px 8px rgba(46,125,50,0.3));
    }}

    /* ═══════════════════════════════════════════════════════════
       METRIC CARDS FOR WEATHER DASHBOARD
       ═══════════════════════════════════════════════════════════ */
    .metric-card {{
        background: linear-gradient(135deg, {COLORS['warm_white']}, {COLORS['morning_dew']});
        border: 2px solid #E0F2F1;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        position: relative;
        overflow: hidden;
    }}
    .metric-card::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 4px;
        background: linear-gradient(90deg, {COLORS['sky_blue']}, {COLORS['leaf_medium']});
        transform: scaleX(0);
        transition: transform 0.4s ease;
    }}
    .metric-card:hover::before {{
        transform: scaleX(1);
    }}
    .metric-card:hover {{
        transform: translateY(-6px) scale(1.03);
        box-shadow: 0 12px 32px rgba(2,136,209,0.2);
        border-color: {COLORS['sky_blue']};
    }}
    .metric-value {{
        font-size: 2rem;
        font-weight: 900;
        color: {COLORS['soil_dark']};
        font-family: 'Merriweather', serif !important;
        margin-bottom: 0.3rem;
    }}
    .metric-label {{
        font-size: 0.85rem;
        color: {COLORS['soil_light']};
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    .metric-icon {{
        font-size: 2.5rem;
        display: block;
        margin-bottom: 0.5rem;
        animation: leafFloat 3s ease-in-out infinite;
    }}

    /* ═══════════════════════════════════════════════════════════
       INFO BOXES WITH ICONS
       ═══════════════════════════════════════════════════════════ */
    .info-box {{
        background: linear-gradient(135deg, {COLORS['crop_yellow']}, #FFFDE7);
        border-left: 5px solid {COLORS['wheat_gold']};
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(249,168,37,0.15);
        animation: slideInRight 0.5s ease-out;
        position: relative;
    }}
    .info-box::before {{
        content: '💡';
        position: absolute;
        top: 10px;
        right: 15px;
        font-size: 1.8rem;
        opacity: 0.3;
        animation: pulse 2s ease-in-out infinite;
    }}
    .info-box strong {{
        color: {COLORS['soil_dark']};
        font-family: 'Merriweather', serif;
    }}

    /* Warning box variant */
    .warning-box {{
        background: linear-gradient(135deg, #FFEBEE, #FFCDD2);
        border-left: 5px solid {COLORS['earth_red']};
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(191,54,12,0.15);
        animation: slideInLeft 0.5s ease-out;
        position: relative;
    }}
    .warning-box::before {{
        content: '⚠️';
        position: absolute;
        top: 10px;
        right: 15px;
        font-size: 1.8rem;
        opacity: 0.3;
        animation: bounce 2s ease-in-out infinite;
    }}
    .warning-box strong {{
        color: {COLORS['earth_red']};
        font-family: 'Merriweather', serif;
    }}
</style>
"""
