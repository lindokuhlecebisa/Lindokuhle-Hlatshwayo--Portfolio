failed_logins = {}

def detect_anomaly(log):
    user = log["user"]
    status = log["status"]
    ip_last = int(log["ip"].split(".")[-1])

    # Rule 1: Track failed logins
    if status == "FAIL":
        failed_logins[user] = failed_logins.get(user, 0) + 1
    else:
        failed_logins[user] = 0

    # Rule 2: Too many failed attempts
    if failed_logins[user] >= 3:
        return f"ALERT: {user} has multiple failed login attempts"

    # Rule 3: Admin failure
    if user == "admin" and status == "FAIL":
        return "CRITICAL ALERT: Admin login failure detected"

    # Rule 4: Suspicious IP range
    if ip_last > 200:
        return f"WARNING: Suspicious IP detected {log['ip']}"

    return None