def parse_log_line(line):
    parts = line.strip().split()

    if len(parts) < 5:
        return None

    return {
        "timestamp": parts[0] + " " + parts[1],
        "event": parts[2],
        "user": parts[3].split("=")[1],
        "ip": parts[4].split("=")[1]
    }


def normalize(parsed):
    return {
        "timestamp": parsed["timestamp"],
        "action": parsed["event"],      # IMPORTANT
        "source_ip": parsed["ip"],
        "user": parsed["user"]
    }