from flask import Blueprint, jsonify
import os
import re
from app.config import LOG_FILE

api_bp = Blueprint("api", __name__)


# ================= ALERTS =================
@api_bp.route("/alerts")
def get_alerts():

    alerts = []

    try:
        if not os.path.exists(LOG_FILE):
            return jsonify([])

        with open(LOG_FILE, "r") as f:
            lines = f.readlines()

        for line in lines:

            # extract IP safely
            ip_match = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
            ip = ip_match.group(0) if ip_match else "Unknown"

            # 🔥 DETECT MULTIPLE ATTACK TYPES
            if "FAILED_LOGIN" in line:
                alerts.append({"type": "FAILED_LOGIN", "ip": ip})

            elif "PORT_SCAN" in line:
                alerts.append({"type": "PORT_SCAN", "ip": ip})

            elif "SQL_INJECTION" in line or "1=1" in line:
                alerts.append({"type": "SQL_INJECTION", "ip": ip})

            elif "XSS" in line or "<script>" in line:
                alerts.append({"type": "XSS_ATTACK", "ip": ip})

            elif "SUSPICIOUS_AGENT" in line or "sqlmap" in line:
                alerts.append({"type": "SCANNER_ACTIVITY", "ip": ip})

    except Exception as e:
        print("ERROR:", e)

    return jsonify(alerts)

# ================= LOGS =================
@api_bp.route("/logs")
def get_logs():

    try:
        if not os.path.exists(LOG_FILE):
            return jsonify([])

        with open(LOG_FILE, "r") as f:
            lines = f.readlines()

        logs = [line.strip() for line in lines if line.strip()]

        return jsonify(logs)

    except Exception as e:
        print("LOG ERROR:", e)
        return jsonify([])