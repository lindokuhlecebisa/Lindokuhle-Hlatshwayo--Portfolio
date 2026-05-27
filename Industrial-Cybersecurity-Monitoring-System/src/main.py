from logger import generate_log
from detector import detect_anomaly
from alerts import send_alert
import time

while True:
    log = generate_log()
    print("LOG:", log)

    with open("logs/logs.txt", "a") as f:
        f.write(str(log) + "\n")

    alert = detect_anomaly(log)

    if alert:
        send_alert(alert, log)

    time.sleep(2)