blacklist = set()

def block_ip(ip):
    blacklist.add(ip)
    return f"Blocked IP: {ip}"