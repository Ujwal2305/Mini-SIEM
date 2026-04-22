import sys
import os
import time
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.log_collector import write_log


def generate_ip():
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"


# 🔥 FORCE ALL TYPES TO APPEAR
def generate_attack(ip):
    attacks = [
        f"FAILED_LOGIN user=admin ip={ip}",
        f"PORT_SCAN ip={ip} port={random.randint(20,1024)}",
        f"SQL_INJECTION ip={ip} payload=' OR 1=1 --",
        f"XSS_ATTACK ip={ip} payload=<script>alert(1)</script>",
        f"SUSPICIOUS_AGENT ip={ip} agent=sqlmap"
    ]

    # 🔥 ensure variety (not stuck on one)
    return random.choice(attacks)


while True:
    ip = generate_ip()

    # 🔥 generate MULTIPLE logs per cycle
    for _ in range(3):
        log = generate_attack(ip)
        write_log(log)
        print(log)

    time.sleep(1)