from collections import defaultdict
import time

failed_logins = defaultdict(list)

def detect_bruteforce(log):

    if log.get("action") == "FAILED_LOGIN":

        ip = log.get("source_ip")

        failed_logins[ip].append(time.time())

        # last 60 sec window
        failed_logins[ip] = [
            t for t in failed_logins[ip] if time.time() - t < 60
        ]

        if len(failed_logins[ip]) >= 3:   # low threshold for demo
            return True, ip

    return False, None