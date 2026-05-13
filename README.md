# 🌾 AgriExpert AI — Your Smart Farming Companion

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/your-repo/agri-expert-ai/main/app.py)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Transform your farming with AI-powered insights!** Get expert advice on crops, soil health, disease diagnosis, and weather—available in 16+ languages.

---

## 🎯 What Can AgriExpert AI Do For You?

<table>
  <tr>
    <td align="center">
      <b>💬 Chat with AI Expert</b><br>
      Ask any farming question<br>
      Get instant answers
    </td>
    <td align="center">
      <b>🧪 Analyze Soil</b><br>
      Input N-P-K values<br>
      Get fertilizer tips
    </td>
    <td align="center">
      <b>📸 Diagnose Diseases</b><br>
      Upload plant photos<br>
      Identify problems
    </td>
    <td align="center">
      <b>🌾 Recommend Crops</b><br>
      Location-based suggestions<br>
      Profit estimates
    </td>
    <td align="center">
      <b>🌦️ Weather Alerts</b><br>
      7-day forecasts<br>
      Frost & rain warnings
    </td>
  </tr>
  <tr>
    <td align="center">🗣️</td>
    <td align="center">🔬</td>
    <td align="center">🩺</td>
    <td align="center">🌱</td>
    <td align="center">⛈️</td>
  </tr>
</table>

---

## ✨ Why Farmers Love AgriExpert AI

### 🌍 **Multilingual Support**
Speak your language! Choose from **16+ languages**:
- 🇮🇳 Hindi, Kannada, Tamil, Telugu, Marathi, Bengali, Punjabi, Gujarati, Urdu
- 🇺🇸 English | 🇪🇸 Spanish | 🇵🇹 Portuguese | 🇫🇷 French | 🇰🇪 Swahili | 🇨🇳 Chinese | 🇮🇩 Indonesian

> 💡 *Technical terms are always shown with English translations for clarity.*

### 🤖 **Powered by Cutting-Edge AI**
- **Llama 3.3 70B** for detailed text conversations
- **Llama 4 Scout** for accurate image-based disease diagnosis
- Real-time weather data from **Open-Meteo** (no API key needed!)

### 🎨 **Beautiful, Intuitive Interface**
- Clean, earthy design inspired by nature
- Easy-to-use tools with one-click actions
- Mobile-friendly and accessible

---

## 🚀 Quick Start Guide

### Step 1: Get Set Up (5 minutes)

```bash
# Clone the repository
git clone https://github.com/your-username/agri-expert-ai.git
cd agri-expert-ai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Get Your Free Groq API Key

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up (it's free!)
3. Generate an API key
4. Copy it—you'll need it in the app!

### Step 3: Run the App

```bash
streamlit run app.py
```

Then open your browser to **`http://localhost:8501`** 🎉

---

## 📖 How to Use Each Feature

<details>
<summary><b>💬 Chat with AI Expert</b> - Click to expand</summary>

1. Enter your Groq API key in the sidebar
2. Type your farming question (e.g., *"How do I prevent tomato blight?"*)
3. Get instant, expert advice with full context awareness

**Pro Tip:** Mention your location or crop type for more personalized answers!
</details>

<details>
<summary><b>🧪 Soil Nutrient Analysis</b> - Click to expand</summary>

1. Select the **Soil Analysis** tool
2. Input your soil test results:
   - Nitrogen (N), Phosphorus (P), Potassium (K) levels
   - pH value
   - Soil type (optional)
3. Click **"Analyze Soil"**
4. Receive customized fertilizer recommendations and improvement plans
</details>

<details>
<summary><b>📸 Leaf & Crop Disease Diagnosis</b> - Click to expand</summary>

1. Select the **Leaf/Crop Disease** tool
2. Upload a clear photo of the affected plant
3. Describe what you're seeing (yellow spots, wilting, etc.)
4. Click **"Diagnose"**
5. Get identification + organic & chemical treatment options

**📸 Photo Tips:** Take pictures in good lighting, focus on affected areas, include both close-up and full plant views.
</details>

<details>
<summary><b>🌾 Smart Crop Recommender</b> - Click to expand</summary>

1. Select the **Crop Recommender** tool
2. Fill in your details:
   - Location (for climate data)
   - Current season
   - Water availability
   - Farm size
   - Irrigation method
3. Get tailored crop suggestions with yield estimates and profit analysis!
</details>

<details>
<summary><b>🌦️ Weather Dashboard</b> - Click to expand</summary>

1. Enter your farm location in the sidebar
2. View the **7-day forecast** with temperature, rainfall, and wind
3. Receive automatic alerts for:
   - ❄️ Frost warnings
   - ⛈️ Heavy rain alerts
4. All AI recommendations automatically factor in weather conditions!
</details>

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Frontend** | [Streamlit](https://streamlit.io) | Interactive web interface |
| **AI Engine** | [Groq API](https://groq.com) | Fast LLM inference |
| **Vision Model** | Llama 4 Scout | Image-based disease diagnosis |
| **Weather Data** | [Open-Meteo](https://open-meteo.com) | Free, accurate forecasts |
| **Image Processing** | Pillow | Photo upload handling |
| **Styling** | Custom CSS + Google Fonts | Beautiful, responsive UI |

---

## 📋 Requirements

- ✅ Python 3.8 or higher
- ✅ Free Groq API key ([get yours here](https://console.groq.com))
- ✅ Internet connection (for weather data & AI)
- ✅ Modern web browser (Chrome, Firefox, Safari, Edge)

---

## 🤝 Contributing

We'd love your help making AgriExpert AI even better! Here's how:

### 🌟 Ways to Contribute
- 🐛 Report bugs or suggest features
- 📝 Improve documentation or translations
- 🌱 Add crop-specific knowledge
- 🔌 Build integrations with agricultural databases
- 🎨 Enhance the UI/UX

### Quick Start for Contributors
```bash
# Fork the repo
git checkout -b feature/your-amazing-idea
# Make your changes
git commit -m "Add amazing new feature"
git push origin feature/your-amazing-idea
# Open a Pull Request!
```

Check out our [Contributing Guidelines](CONTRIBUTING.md) for more details.

---

## ❓ FAQ

<details>
<summary><b>Is this really free?</b></summary>
Yes! The app is free and open-source. You only need a free Groq API key (they offer generous free tiers).
</details>

<details>
<summary><b>How accurate is the disease diagnosis?</b></summary>
Our AI model achieves high accuracy on common crop diseases, but we always recommend confirming with local agricultural experts for critical decisions.
</details>

<details>
<summary><b>Can I use this offline?</b></summary>
Currently, an internet connection is required for AI inference and weather data. Offline capabilities are planned for future releases!
</details>

<details>
<summary><b>My language isn't listed. Can you add it?</b></summary>
We support 16+ major languages already, but we're always expanding! Open an issue with your language request.
</details>

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — feel free to use, modify, and distribute!

---

## 🙏 Acknowledgments

Special thanks to:
- 🚀 **[Groq](https://groq.com)** for lightning-fast, affordable AI inference
- 🌤️ **[Open-Meteo](https://open-meteo.com)** for free, reliable weather data
- 📊 **[Streamlit](https://streamlit.io)** for the amazing web app framework
- 👨‍🌾 **Farmers worldwide** for their invaluable knowledge and feedback

---

## 📞 Need Help?

- 🐛 Found a bug? [Open an issue](https://github.com/your-username/agri-expert-ai/issues)
- 💬 Have questions? Check our [Wiki](https://github.com/your-username/agri-expert-ai/wiki)
- 📧 Contact the maintainers via GitHub

---

<div align="center">

### 🌾 Built with ❤️ for farmers, by developers who care about sustainable agriculture.

**Star ⭐ this repo if you find it useful!**

[Report Bug](https://github.com/your-username/agri-expert-ai/issues) · [Request Feature](https://github.com/your-username/agri-expert-ai/issues) · [View Demo](https://share.streamlit.io/your-repo/agri-expert-ai/main/app.py)

</div>
