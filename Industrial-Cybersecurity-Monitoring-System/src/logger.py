import time
import random

def generate_log():
    users = ["operator1", "operator2", "admin", "guest"]
    actions = ["login", "file_access", "machine_start", "machine_stop", "config_change"]
    status = ["SUCCESS", "FAIL"]

    log = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "user": random.choice(users),
        "action": random.choice(actions),
        "status": random.choice(status),
        "ip": f"192.168.1.{random.randint(1, 255)}"
    }

    return log