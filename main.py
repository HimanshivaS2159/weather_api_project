from flask import Flask, render_template, request, redirect, session
import json
import requests

app = Flask(__name__)

app.secret_key = "skysense_secret_key"

API_KEY = "5145f1e1b614ff001ee79a48c37bd5fc"


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

          return """
    <script>
    alert('Username must be at least 4 characters');
    window.location.href='/register';
    </script>
    """
        mobile = request.form["mobile"]
        dob = request.form["dob"]
        password = request.form["password"]
        if len(password) < 8:
         return """
    <script>
    alert('Password must be at least 8 characters long');
    window.location.href='/register';
    </script>
    """

        if not any(char.isdigit() for char in password):
          return """
    <script>
    alert('Password must contain at least one number');
    window.location.href='/register';
    </script>
    """

        with open("users.json", "r") as file:
            users = json.load(file)

        for user in users:
            if user["username"] == username:
                return """
                <script>
                alert('Username already exists');
                window.location.href='/register';
                </script>
                """

        users.append({
            "name": name,
            "username": username,
            "mobile": mobile,
            "dob": dob,
            "password": password
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

        for user in users:

            if user["username"] == username and user["password"] == password:

                session["username"] = username

                return redirect("/dashboard")

        return """
        <script>
        alert('Invalid Username or Password');
        window.location.href='/login';
        </script>
        """

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

        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        data = response.json()

        if "main" in data:

            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "wind": data["wind"]["speed"],
                "condition": data["weather"][0]["description"].title()
            }

        else:

            return """
            <script>
            alert('City not found');
            window.location.href='/dashboard';
            </script>
            """

    return render_template(
        "dashboard.html",
        user=current_user,
        weather=weather
    )


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

          return """
        <script>
        alert('New Password must be at least 8 characters long');
        window.location.href='/edit-profile';
        </script>
        """

        if old_password != "":

            if old_password != current_user["password"]:

                return """
                <script>
                alert('Current Password Incorrect');
                window.location.href='/edit-profile';
                </script>
                """

            if new_password != confirm_password:

                return """
                <script>
                alert('Passwords Do Not Match');
                window.location.href='/edit-profile';
                </script>
                """

            current_user["password"] = new_password

        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)

        return redirect("/dashboard")

    return render_template(
        "edit_profile.html",
        user=current_user
    )
# LOGOUT
@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)