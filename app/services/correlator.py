def correlate(parsed_logs):
    last = [log["action"] for log in parsed_logs[-5:]]

    if "FAILED_LOGIN" in last and "SUCCESS_LOGIN" in last:
        return "BRUTE_FORCE_SUCCESS"

    return None