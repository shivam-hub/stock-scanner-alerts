# chartink_alerts/alert_manager.py
import os
import json
from .config import ALERT_TRACK_FILE, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
import requests
import time

def send_telegram_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Telegram alert sent successfully.")
        else:
            print(f"Failed to send Telegram alert: {response.text}")
        time.sleep(1)
    except Exception as e:
        print("Error sending Telegram alert:", e)

def load_alerts():
    if os.path.exists(ALERT_TRACK_FILE):
        with open(ALERT_TRACK_FILE, "r") as file:
            return json.load(file)
    return {}

def save_alerts(alerts):
    with open(ALERT_TRACK_FILE, "w") as file:
        json.dump(alerts, file)
