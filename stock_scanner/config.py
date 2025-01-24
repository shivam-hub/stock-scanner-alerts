import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

CHARTINK_LINK = 'https://chartink.com/screener/'
CHARTINK_SCAN_URL = 'https://chartink.com/screener/process'
CHARTINK_CONDITION = os.getenv("CHARTINK_CONDITION")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
MONGODB_URI = os.getenv("MONGODB_URI") 
MONGODB_USERNAME=urllib.parse.quote_plus(os.getenv('MONGODB_USERNAME'))
MONGODB_PASSWORD=urllib.parse.quote_plus(os.getenv('MONGODB_PASSWORD'))
MONGODB_APPNAME=os.getenv('MONGODB_APPNAME')
MONGODB_CLUSTER=os.getenv('MONGODB_CLUSTER')

