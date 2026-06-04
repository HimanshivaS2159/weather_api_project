# 🌤️ SkySense - Weather Intelligence Dashboard

A modern, feature-rich weather dashboard with AI-powered chatbot for weather insights and queries.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 🌍 Weather Dashboard
- **Real-time Weather Data** - Live data from OpenWeatherMap API
- **City Search** - Smart suggestions with flag emojis and keyboard navigation
- **My Location** - Auto-detect weather using browser geolocation
- **Recent Searches** - Quick access to previously searched cities
- **Temperature Toggle** - Switch between Celsius and Fahrenheit instantly
- **7-Day Forecast** - Dynamic weekly weather outlook
- **Interactive Charts** - Bar charts and donut charts using Chart.js
- **Google Maps Integration** - Embedded maps with styled UI
- **Fun Insights** - Smart weather recommendations
- **Gauge Visualizations** - Visual indicators for humidity, wind, visibility

### 🤖 AI Weather Assistant (NEW!)
- **Groq AI Integration** - Powered by LLaMA 3.1-8b-instant model
- **Table Support** - Beautiful formatted tables for comparisons
- **Rich Formatting** - Bold, italic, code blocks, and lists
- **Typing Indicator** - Animated 3-dot loading animation
- **Floating Chat Button** - Easy access from anywhere
- **Smart Responses** - Context-aware weather advice
- **Mobile Responsive** - Works on all devices

### 👤 User Management
- **Secure Authentication** - Login/Register system
- **Profile Management** - Edit name, mobile, DOB, password
- **Welcome Messages** - Personalized greetings for new/returning users
- **Session Management** - Secure Flask sessions

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/HimanshivaS2159/weather_api_project.git
   cd weather_api_project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Copy the example file:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Get API Keys**
   - **Groq API**: Visit [console.groq.com](https://console.groq.com/) and create a free account
   - **OpenWeatherMap**: Visit [openweathermap.org/api](https://openweathermap.org/api) (already configured)

5. **Run the application**
   ```bash
   python main.py
   ```

6. **Open in browser**
   ```
   http://localhost:5000
   ```

## 📖 Documentation

- **[Chatbot Setup Guide](CHATBOT_SETUP.md)** - Complete chatbot configuration
- **[Example Questions](CHATBOT_EXAMPLES.md)** - 20+ chatbot examples with table comparisons

## 🎨 Screenshots

### Dashboard
Light theme dashboard with weather cards, charts, and maps.

### AI Chatbot
Floating chat button with intelligent weather assistant that creates tables for comparisons.

## 🎯 Usage

### Searching Weather
1. Login to your account
2. Type a city name in the search box
3. See suggestions with flags and country codes
4. Press Enter or click Search
5. View detailed weather data, charts, and map

### Using the Chatbot
1. Click the blue floating button (bottom-right)
2. Ask weather questions:
   - "What does humidity mean?"
   - "Compare sunny and rainy weather in table format"
   - "Should I carry an umbrella today?"
3. Get instant AI-powered responses with formatted tables

### Temperature Toggle
- Click °C/°F buttons to switch units
- All temperature values update instantly
- Choice saved in browser localStorage

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Charts**: Chart.js
- **Maps**: Google Maps Embed API
- **Weather API**: OpenWeatherMap
- **AI**: Groq API (LLaMA 3.1)
- **Storage**: JSON files

## 📁 Project Structure

```
weather_api_project/
├── main.py                  # Flask application
├── templates/
│   ├── dashboard.html       # Main dashboard with chatbot
│   ├── login.html          # Login page
│   ├── register.html       # Registration page
│   └── edit_profile.html   # Profile editing
├── users.json              # User data storage
├── .env                    # Environment variables (not in git)
├── .env.example           # Environment template
├── requirements.txt       # Python dependencies
├── CHATBOT_SETUP.md      # Chatbot documentation
├── CHATBOT_EXAMPLES.md   # Example questions
└── README.md             # This file
```

## 🔐 Security

- API keys stored in environment variables
- `.env` file excluded from git via `.gitignore`
- Session-based authentication
- Password validation (8+ chars, must include number)
- Username validation (4+ chars)

## 🎨 Design Features

- **Light Theme** - Clean, modern interface
- **Inter Font** - Professional typography
- **Gradient Accents** - Blue gradient for primary actions
- **Smooth Animations** - Fade-ups, hover effects, transitions
- **Responsive Design** - Works on desktop, tablet, mobile
- **Accessibility** - Semantic HTML, proper contrast ratios

## 📊 API Limits

- **OpenWeatherMap**: 1000 calls/day (free tier)
- **Groq API**: Check your plan limits at console.groq.com

## 🐛 Troubleshooting

### Chatbot not working?
1. Check `.env` file has `GROQ_API_KEY`
2. Restart Flask: `Ctrl+C` then `python main.py`
3. Clear browser cache: `Ctrl+Shift+R`
4. Check browser console (F12) for errors

### Weather data not loading?
1. Check internet connection
2. Verify city name spelling
3. Try using "My Location" button

### Can't login?
1. Make sure you've registered first
2. Check username is 4+ characters
3. Check password is 8+ characters with a number

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 👏 Acknowledgments

- **OpenWeatherMap** - Weather data API
- **Groq** - AI inference platform
- **Chart.js** - Beautiful charts
- **Google Maps** - Map integration

## 📧 Contact

- **GitHub**: [@HimanshivaS2159](https://github.com/HimanshivaS2159)
- **Project**: [weather_api_project](https://github.com/HimanshivaS2159/weather_api_project)

---

Made with ❤️ using Flask and Groq AI
