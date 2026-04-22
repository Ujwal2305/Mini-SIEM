from flask import Blueprint, render_template, session, redirect, Response, jsonify, request
import os

main_bp = Blueprint("main", __name__)

LOG_PATH = "logs/system.log"


# ---------------------------
# DASHBOARD (LOGIN REQUIRED)
# ---------------------------
@main_bp.route("/")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    return render_template("dashboard.html")


# ---------------------------
# VIEW LOGS (FOR FRONTEND)
# ---------------------------
@main_bp.route("/logs/system.log")
def get_logs():
    if "user" not in session:
        return redirect("/login")

    try:
        with open(LOG_PATH, "r") as f:
            return Response(f.read(), mimetype="text/plain")
    except FileNotFoundError:
        return "No logs found."


# ---------------------------
# CLEAR LOGS (NEW FEATURE)
# ---------------------------
@main_bp.route("/clear-logs", methods=["POST"])
def clear_logs():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    try:
        with open(LOG_PATH, "w") as f:
            f.write("")   # clear file

        return jsonify({"status": "Logs cleared successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------------------
# LOGOUT
# ---------------------------
@main_bp.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


# ---------------------------
# HEALTH CHECK
# ---------------------------
@main_bp.route("/health")
def health():
    return {
        "status": "running",
        "logged_in": "user" in session
    }


# ---------------------------
# OPTIONAL: DEBUG ROUTE
# ---------------------------
@main_bp.route("/debug")
def debug():
    return {
        "log_exists": os.path.exists(LOG_PATH),
        "log_size": os.path.getsize(LOG_PATH) if os.path.exists(LOG_PATH) else 0
    }