from flask import Flask, render_template, request, redirect, session, jsonify
import json
import requests
import os

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv not installed, use system environment variables

app = Flask(__name__)
app.secret_key = "skysense_secret_key"
API_KEY = "5145f1e1b614ff001ee79a48c37bd5fc"

# Groq API key - Set as environment variable or in .env file
# For local development, set: export GROQ_API_KEY="your_key_here"
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")


@app.route("/")
def home():
    return redirect("/login")


# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        if len(username) < 4:
            return """<script>alert('Username must be at least 4 characters');window.location.href='/register';</script>"""
        mobile = request.form["mobile"]
        dob = request.form["dob"]
        password = request.form["password"]
        if len(password) < 8:
            return """<script>alert('Password must be at least 8 characters long');window.location.href='/register';</script>"""
        if not any(char.isdigit() for char in password):
            return """<script>alert('Password must contain at least one number');window.location.href='/register';</script>"""

        with open("users.json", "r") as file:
            users = json.load(file)

        for user in users:
            if user["username"] == username:
                return """<script>alert('Username already exists');window.location.href='/register';</script>"""

        users.append({
            "name": name,
            "username": username,
            "mobile": mobile,
            "dob": dob,
            "password": password,
            "is_new": True
        })

        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)

        return redirect("/login")

    return render_template("register.html")


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        with open("users.json", "r") as file:
            users = json.load(file)

        for i, user in enumerate(users):
            if user["username"] == username and user["password"] == password:
                session["username"] = username
                # mark as no longer new after first login
                if user.get("is_new"):
                    users[i]["is_new"] = False
                    with open("users.json", "w") as f:
                        json.dump(users, f, indent=4)
                return redirect("/dashboard")

        return render_template("login.html", error=True)

    return render_template("login.html")


# DASHBOARD
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "username" not in session:
        return redirect("/login")

    with open("users.json", "r") as file:
        users = json.load(file)

    current_user = None
    for user in users:
        if user["username"] == session["username"]:
            current_user = user
            break

    weather = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        lat = request.form.get("lat", "")
        lon = request.form.get("lon", "")

        if lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        else:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        if "main" in data:
            temp_c = round(data["main"]["temp"], 1)
            temp_f = round(temp_c * 9/5 + 32, 1)
            feels_c = round(data["main"]["feels_like"], 1)
            feels_f = round(feels_c * 9/5 + 32, 1)
            weather = {
                "city": data["name"],
                "country": data.get("sys", {}).get("country", ""),
                "temperature_c": temp_c,
                "temperature_f": temp_f,
                "feels_c": feels_c,
                "feels_f": feels_f,
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "wind": data["wind"]["speed"],
                "condition": data["weather"][0]["description"].title(),
                "icon": data["weather"][0]["icon"],
                "visibility": round(data.get("visibility", 0) / 1000, 1),
                "lat": data["coord"]["lat"],
                "lon": data["coord"]["lon"],
            }
        else:
            return """<script>alert('City not found. Please check the name and try again.');window.location.href='/dashboard';</script>"""

    is_new = current_user.get("is_new", False)

    return render_template(
        "dashboard.html",
        user=current_user,
        weather=weather,
        is_new=is_new
    )


# WEATHER BY COORDS (AJAX)
@app.route("/weather-by-coords", methods=["POST"])
def weather_by_coords():
    if "username" not in session:
        return jsonify({"error": "unauthorized"}), 401
    data = request.get_json()
    lat = data.get("lat")
    lon = data.get("lon")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    resp = requests.get(url)
    d = resp.json()
    if "main" in d:
        temp_c = round(d["main"]["temp"], 1)
        temp_f = round(temp_c * 9/5 + 32, 1)
        feels_c = round(d["main"]["feels_like"], 1)
        feels_f = round(feels_c * 9/5 + 32, 1)
        return jsonify({
            "city": d["name"],
            "country": d.get("sys", {}).get("country", ""),
            "temperature_c": temp_c,
            "temperature_f": temp_f,
            "feels_c": feels_c,
            "feels_f": feels_f,
            "humidity": d["main"]["humidity"],
            "pressure": d["main"]["pressure"],
            "wind": d["wind"]["speed"],
            "condition": d["weather"][0]["description"].title(),
            "icon": d["weather"][0]["icon"],
            "visibility": round(d.get("visibility", 0) / 1000, 1),
            "lat": d["coord"]["lat"],
            "lon": d["coord"]["lon"],
        })
    return jsonify({"error": "not found"}), 404


# EDIT PROFILE
@app.route("/edit-profile", methods=["GET", "POST"])
def edit_profile():
    if "username" not in session:
        return redirect("/login")

    with open("users.json", "r") as file:
        users = json.load(file)

    current_user = None
    for user in users:
        if user["username"] == session["username"]:
            current_user = user
            break

    if request.method == "POST":
        current_user["name"] = request.form["name"]
        current_user["mobile"] = request.form["mobile"]
        current_user["dob"] = request.form["dob"]

        old_password = request.form["old_password"]
        new_password = request.form["new_password"]
        confirm_password = request.form["confirm_password"]

        if old_password != "":
            if len(new_password) < 8:
                return """<script>alert('New Password must be at least 8 characters long');window.location.href='/edit-profile';</script>"""
            if old_password != current_user["password"]:
                return """<script>alert('Current Password Incorrect');window.location.href='/edit-profile';</script>"""
            if new_password != confirm_password:
                return """<script>alert('Passwords Do Not Match');window.location.href='/edit-profile';</script>"""
            current_user["password"] = new_password

        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)

        return redirect("/dashboard")

    return render_template("edit_profile.html", user=current_user)


# LOGOUT
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/login")


# CHATBOT ENDPOINT (Groq API)
@app.route("/chat", methods=["POST"])
def chat():
    if "username" not in session:
        return jsonify({"error": "unauthorized"}), 401
    
    data = request.get_json()
    user_message = data.get("message", "").strip()
    
    if not user_message:
        return jsonify({"error": "empty message"}), 400
    
    if not GROQ_API_KEY:
        return jsonify({"error": "Groq API key not configured. Please set GROQ_API_KEY environment variable."}), 500
    
    try:
        # Call Groq API
        groq_response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama-3.1-8b-instant",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are SkySense Weather Assistant, a helpful and friendly weather chatbot. You help users understand weather data, give weather advice, explain meteorological terms, and answer questions about weather conditions. Keep responses concise, friendly, and informative.\n\nWhen comparing data or showing multiple items, use markdown table format like this:\n| Column 1 | Column 2 |\n|----------|----------|\n| Data 1   | Data 2   |\n\nUse **bold** for emphasis, `code` for technical terms, and bullet points with - for lists."
                    },
                    {
                        "role": "user",
                        "content": user_message
                    }
                ],
                "temperature": 0.7,
                "max_tokens": 600
            },
            timeout=30
        )
        
        if groq_response.status_code == 200:
            result = groq_response.json()
            bot_reply = result["choices"][0]["message"]["content"]
            return jsonify({"reply": bot_reply})
        else:
            # Return detailed error for debugging
            error_detail = groq_response.text
            return jsonify({"error": f"Groq API error {groq_response.status_code}: {error_detail}"}), 500
            
    except requests.exceptions.Timeout:
        return jsonify({"error": "Request timeout"}), 504
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
