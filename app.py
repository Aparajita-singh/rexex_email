from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

# Sample User Data (replace with actual login/signup implementation)
users = {"user1": "password1", "user2": "password2"}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            return redirect(url_for("profile", username=username))
        else:
            return render_template(
                "login.html", error="Invalid credentials. Please try again."
            )
    return render_template("login.html", error=None)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users[username] = password
        return redirect(url_for("profile", username=username))
    return render_template("signup.html")


@app.route("/profile/<username>")
def profile(username):
    return render_template("profile.html", username=username)


@app.route("/regex_match", methods=["GET", "POST"])
def regex_match():
    matched_strings = []
    if request.method == "POST":
        test_string = request.form["test_string"]
        regex_pattern = request.form["regex_pattern"]
        matched_strings = re.findall(regex_pattern, test_string)
    return render_template("regex_form.html", matched_strings=matched_strings)


@app.route("/email_validation", methods=["GET", "POST"])
def email_validation():
    is_valid = None
    if request.method == "POST":
        email = request.form["email"]
        is_valid = validate_email(email)
    return render_template("email_form.html", is_valid=is_valid)


def validate_email(email):
    # Simple email validation, replace with your own logic
    return re.match(r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$", email) is not None


if __name__ == "__main__":
    app.run(debug=True)
