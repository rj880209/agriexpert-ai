"""
Configuration and constants for AgriExpert AI
"""

# App Configuration
APP_CONFIG = {
    "page_title": "AgriExpert AI — Smart Farming Assistant",
    "page_icon": "🌾",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
}

# Color Palette - Earthy Farming Aesthetic
COLORS = {
    # Soil tones
    "soil_dark": "#3E2723",
    "soil_medium": "#5D4037",
    "soil_light": "#8D6E63",
    # Leaf greens
    "leaf_dark": "#2E7D32",
    "leaf_medium": "#43A047",
    "leaf_light": "#66BB6A",
    # Wheat golds
    "wheat_gold": "#F9A825",
    "wheat_light": "#FDD835",
    # Accents
    "sunrise_orange": "#EF6C00",
    "sky_blue": "#0288D1",
    # Backgrounds
    "cream": "#FFF8E1",
    "warm_white": "#FFFDF5",
    "parchment": "#F5F0E1",
    "field_green": "#E8F5E9",
}

# Language Options
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

# Weather Thresholds
WEATHER_THRESHOLDS = {
    "frost_warning": 2,  # °C
    "frost_severe": -2,  # °C
    "heavy_rain_warning": 20,  # mm
    "heavy_rain_severe": 50,  # mm
}

# Groq Model Configuration
MODEL_CONFIG = {
    "chat_model": "llama-3.3-70b-versatile",
    "vision_model": "meta-llama/llama-4-scout-17b-16e-instruct",
    "temperature_chat": 0.6,
    "temperature_vision": 0.5,
    "max_tokens": 2048,
}

# Tool Options
TOOL_OPTIONS = [
    "💬 Chat",
    "🧪 Soil Analysis",
    "📸 Leaf Diagnosis",
    "🌾 Crop Recommender",
    "🌦️ Weather Dashboard",
]

# Quick-start chat prompts
QUICK_START_CARDS = [
    ("🌱", "Crop Selection", "Best crops for my region & season", "What should I plant this season?"),
    ("💧", "Irrigation", "Smart watering schedules", "How often should I water my wheat?"),
    ("🐛", "Pest Control", "Disease identification & treatment", "Yellow spots on my tomato leaves"),
    ("🌦️", "Weather Advice", "Prepare for upcoming conditions", "How should I prepare for the upcoming weather?"),
]

# Session state defaults
SESSION_DEFAULTS = {
    "messages": [],
    "groq_api_key": "",
    "weather_context": "",
    "weather_alerts": None,
    "weather_location": "",
    "language": "English",
}
