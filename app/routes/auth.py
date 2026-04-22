from flask import Blueprint, render_template, request, redirect, session, url_for

auth_bp = Blueprint("auth", __name__)

USER = {
    "username": "admin",
    "password": "admin123"
}

@auth_bp.route("/login", methods=["GET", "POST"])
def web_login():

    if request.method == "POST":
        if request.form["username"] == USER["username"] and request.form["password"] == USER["password"]:
            session["user"] = USER["username"]
            return redirect(url_for("main.dashboard"))

        return "Invalid credentials"

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")