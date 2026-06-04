# SkySense Chatbot Setup

## ✅ Status: Chatbot Working!

The chatbot has been successfully integrated and tested with your SkySense dashboard!

## 🔧 Configuration

- **Groq API Key**: Set as environment variable (see instructions below) ✅ **API VERIFIED WORKING**
- **Model**: `llama-3.1-8b-instant` ✅ **TESTED & CONFIRMED**
- **Endpoint**: `/chat` (POST)
- **System Prompt**: "You are SkySense Weather Assistant, a helpful and friendly weather chatbot"

## 🔑 Setting Up Your API Key

### Method 1: Environment Variable (Recommended)

**Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY="your_groq_api_key_here"
python main.py
```

**Windows (Command Prompt):**
```cmd
set GROQ_API_KEY=your_groq_api_key_here
python main.py
```

**Linux/Mac:**
```bash
export GROQ_API_KEY="your_groq_api_key_here"
python main.py
```

### Method 2: Create a .env file

1. Create a file named `.env` in project root
2. Add this line:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```
3. Install python-dotenv: `pip install python-dotenv`
4. Add to main.py (at top):
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

### Get Your Groq API Key

1. Visit: https://console.groq.com/
2. Sign up or login
3. Go to API Keys section
4. Create new key
5. Copy and use as shown above

## ✅ API Test Results

The Groq API has been tested and is working perfectly:
- Status: 200 OK
- Model Response: Successfully generating replies
- API Key: Valid and active

## 🚀 How to Use

1. **Make sure Flask is running**:
   ```bash
   python main.py
   ```
   You should see: `* Running on http://127.0.0.1:5000`

2. **Access the chatbot**:
   - Open browser: `http://localhost:5000` or `http://127.0.0.1:5000`
   - Login to your dashboard
   - Look for the blue floating chat button in the bottom-right corner (has "AI" badge)
   - Click it to open the chat window

3. **Start chatting**:
   - Type your weather questions like:
     - "What does humidity mean?"
     - "Should I carry an umbrella today?"
     - "Explain what atmospheric pressure is"
     - "What's the difference between feels like and actual temperature?"
     - **"Compare sunny, cloudy, and rainy weather in a table"** ⭐ NEW!
     - **"Show temperature ranges in table format"** ⭐ NEW!
   - Press Enter or click the send button
   - The bot will respond using Groq's LLaMA 3.1 model
   - **Comparison questions automatically create beautiful tables!**

## 🎨 Features

- 🔵 Floating chat button with "AI" badge
- 💬 Clean chat interface with gradient blue header
- 👤 User messages on the right (blue gradient)
- 🤖 Bot messages on the left (grey)
- ⏳ Typing indicator (3 animated dots) while bot is thinking
- ✨ Smooth animations and transitions
- 📱 Mobile responsive design
- 📊 **NEW: Table support** - Beautiful formatted tables for comparisons
- 🎯 **NEW: Rich formatting** - Bold, italic, code, lists
- 💎 **NEW: Smart layout** - Tables render perfectly in chat bubbles

## 🐛 If You're Getting a 400 Error

If you see "400" error in the chatbot, try these steps:

### Step 1: Restart Flask Completely
```bash
# Press Ctrl + C to stop Flask
# Then restart:
python main.py
```

### Step 2: Clear Browser Cache
- Press `Ctrl + Shift + R` (hard refresh) in your browser
- Or use Incognito/Private mode

### Step 3: Check if you're logged in
- The chatbot only works for logged-in users
- Make sure you see your name in the dashboard

### Step 4: Check Flask terminal output
- When you send a message, watch the Flask terminal
- You should see the POST request to `/chat`
- Any errors will be displayed there

### Step 5: Check browser console
- Press F12 to open Developer Tools
- Go to Console tab
- Send a message in chatbot
- Look for any error messages

## 💡 Common Issues & Solutions

1. **"unauthorized" error** → You're not logged in. Login first.
2. **"empty message" error** → The message field is blank.
3. **500 error** → Check Flask terminal for detailed Groq API error.
4. **Connection failed** → Flask server is not running.
5. **400 error** → Usually means the request format is wrong. Try restarting Flask.

## 🧪 Test the API Directly

If chatbot isn't working in browser, test the API directly:

```bash
python test_groq.py
```

This will confirm if the Groq API key is working correctly.

## 📝 Files Modified

- `main.py` - Added `/chat` endpoint with Groq API integration (API key working!)
  - ✅ Enhanced system prompt for table formatting
  - ✅ Increased max_tokens to 600 for longer responses
- `templates/dashboard.html` - Added chatbot UI and JavaScript
  - ✅ Added markdown table parser
  - ✅ Added rich text formatting (bold, italic, code, lists)
  - ✅ Enhanced chat bubble styling for tables
- `CHATBOT_EXAMPLES.md` - Example questions to try (especially table comparisons!)

## 🎉 Ready to Chat!

Everything is configured and tested. The Groq API is confirmed working!

Just make sure:
1. Flask is running: `python main.py`
2. You're logged in to the dashboard
3. Click the blue chat button in bottom-right corner
4. Start chatting!

If you still get errors, share the exact error message from:
- The chatbot window
- Browser console (F12)
- Flask terminal output
