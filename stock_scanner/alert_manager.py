from .config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, MONGODB_USERNAME, MONGODB_PASSWORD, MONGODB_APPNAME, MONGODB_CLUSTER
import requests
import time
from datetime import datetime
from pymongo import MongoClient

MONGO_CONN='mongodb+srv://%s:%s@%s.awl7l.mongodb.net/?retryWrites=true&w=majority&appName=%s' % (MONGODB_USERNAME, MONGODB_PASSWORD, MONGODB_CLUSTER, MONGODB_APPNAME)
print(MONGO_CONN)
client = MongoClient(MONGO_CONN)
# client = MongoClient('mongodb+srv://%s:%s@%s.awl7l.mongodb.net/?retryWrites=true&w=majority&appName=%s' % (MONGODB_USERNAME, MONGODB_PASSWORD, MONGODB_CLUSTER, MONGODB_APPNAME))
db = client['stock_alerts_db']
alerts_collection = db['alerts_sent'] 

def send_telegram_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {'chat_id': TELEGRAM_CHAT_ID, 'text': message, 'parse_mode' : 'HTML'}
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            time.sleep(1)
            return True
        else:
            time.sleep(1)
            print(f"Failed to send Telegram alert: {response.text}")
            return False
    except Exception as e:
        print("Error sending Telegram alert:", e)
        return False

def load_alerts():
    today = datetime.now().strftime("%Y-%m-%d")
    alerts = alerts_collection.find_one({"date": today})
    if alerts:
        return alerts["stocks"]
    return []

def save_alerts(alerts, alert_failed):
    today = datetime.now().strftime("%Y-%m-%d")
    alerts_collection.update_one(
        {"date": today},
        {"$set": {"date": today, "stocks": alerts, "alert_failed" : alert_failed}},
        upsert=True
    )
