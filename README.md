# 🌾 AgriExpert AI — Smart Farming Assistant

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/your-repo/agri-expert-ai/main/app.py)

**AgriExpert AI** is an intelligent, AI-powered farming assistant designed to help farmers maximize crop yields, manage soil health, diagnose plant diseases, and adapt to weather conditions. Built with cutting-edge AI models from Groq, it provides personalized, data-driven advice in multiple languages.

## ✨ Key Features

### 💬 Conversational Chat
- Ask any farming-related question with full conversational context.
- Get expert advice on crop selection, irrigation, pest control, and more.
- AI remembers previous interactions for personalized recommendations.

### 🧪 Soil Nutrient Analysis
- Input N-P-K values and pH levels for instant soil health assessment.
- Receive tailored fertilizer recommendations and soil improvement plans.
- Supports different soil types and target crops.

### 📸 Leaf & Crop Disease Diagnosis
- Upload photos of sick plants for AI-powered visual diagnosis.
- Identify pests, diseases, and nutrient deficiencies with high accuracy.
- Get organic and chemical treatment options with safety warnings.

### 🌾 Smart Crop Recommender
- Get crop suggestions based on location, climate, season, and water availability.
- Includes yield estimates, cost-profit analysis, and risk assessments.
- Factors in farm size and irrigation capabilities.

### 🌦️ Weather Dashboard & Alerts
- Real-time 7-day weather forecasts with frost and heavy rain alerts.
- Automatic integration of weather data into all AI recommendations.
- Visual dashboard showing temperature, rainfall, and wind conditions.

### 🌐 Multi-Language Support
- Responds in 16+ languages including English, Hindi, Kannada, Tamil, Telugu, Marathi, Bengali, Punjabi, Gujarati, Urdu, Spanish, Portuguese, French, Swahili, Chinese, and Indonesian.
- Technical terms remain clear with English translations.

## 🏗️ How It Works

AgriExpert AI leverages advanced AI models to provide comprehensive farming assistance:

1. **AI Models**: Uses Groq's `llama-3.3-70b-versatile` for text-based interactions and `meta-llama/llama-4-scout-17b-16e-instruct` for image analysis.

2. **Weather Integration**: Fetches real-time weather data from Open-Meteo API (free, no API key required) to provide weather-aware advice.

3. **System Prompt Engineering**: Employs a detailed system prompt that defines the AI as a senior agronomist, ensuring accurate and practical recommendations.

4. **Session Management**: Maintains conversation history and user preferences across interactions.

5. **Safety & Compliance**: Includes disclaimers for pesticide and fertilizer use, emphasizing local regulations.

## 🛠️ Technologies Used

- **Frontend**: Streamlit - for building the interactive web app
- **AI Engine**: Groq API - for LLM and vision model inference
- **Weather Data**: Open-Meteo API - for location-based forecasts
- **Image Processing**: Pillow - for handling uploaded images
- **HTTP Requests**: Requests library - for API calls
- **Styling**: Custom CSS with Google Fonts for an earthy, farming-themed UI

## 📋 Prerequisites

- Python 3.8 or higher
- A free Groq API key (sign up at [console.groq.com](https://console.groq.com))
- Internet connection for weather data and AI inference

## 🚀 Installation & Setup

1. **Clone or download the repository**:
   ```bash
   git clone https://github.com/your-username/agri-expert-ai.git
   cd agri-expert-ai
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Get your Groq API key**:
   - Visit [console.groq.com](https://console.groq.com)
   - Sign up for a free account
   - Generate an API key

5. **Run the application**:
   ```bash
   streamlit run app.py
   ```

6. **Access the app**:
   - Open your browser to `http://localhost:8501`
   - Enter your Groq API key in the sidebar
   - Start chatting!

## 📖 Usage Guide

### Getting Started
1. Enter your Groq API key in the sidebar.
2. (Optional) Set your preferred language for AI responses.
3. (Optional) Enter your farm location to enable weather alerts.

### Using the Tools
- **Chat**: Type your farming question in the chat input or click quick-start cards.
- **Soil Analysis**: Input your soil test values and click "Analyze Soil".
- **Leaf Diagnosis**: Upload a plant photo and describe symptoms, then click "Diagnose".
- **Crop Recommender**: Fill in your location, season, and conditions, then get recommendations.
- **Weather Dashboard**: View your 7-day forecast and get AI analysis.

### Tips for Best Results
- Provide specific details (location, crop type, symptoms) for more accurate advice.
- Use the weather integration for proactive farming decisions.
- Upload clear, well-lit photos for disease diagnosis.

## 🤝 Contributing

We welcome contributions to improve AgriExpert AI! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Improvement
- Add more crop-specific knowledge
- Implement offline capabilities
- Expand language support
- Add integration with local agricultural databases

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Groq** for providing fast, affordable AI inference
- **Open-Meteo** for free weather data
- **Streamlit** for the amazing web app framework
- Farmers worldwide for their invaluable knowledge and feedback

## 📞 Support

If you encounter issues or have suggestions:
- Open an issue on GitHub
- Check the troubleshooting section in our wiki
- Contact the maintainers

---

**Built with ❤️ for farmers, by developers who care about sustainable agriculture.**
