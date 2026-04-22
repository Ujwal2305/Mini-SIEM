from app.config import LOG_FILE
import os

def write_log(log):

    # ensure folder exists
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    # ✅ ALWAYS APPEND
    with open(LOG_FILE, "a") as f:
        f.write(log.strip() + "\n")