# chartink_alerts/config.py
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration variables
CHARTINK_LINK = 'https://chartink.com/screener/'
CHARTINK_SCAN_URL = 'https://chartink.com/screener/process'
CHARTINK_CONDITION = os.getenv("CHARTINK_CONDITION")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

ALERT_TRACK_FILE = "../alerts_sent.json"
