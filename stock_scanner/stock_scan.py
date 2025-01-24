import requests
import pandas as pd
from bs4 import BeautifulSoup
from .config import CHARTINK_LINK, CHARTINK_SCAN_URL

def GetDataFromChartink(payload):
    payload = "scan_clause=" + payload

    with requests.Session() as s:
        r = s.get(CHARTINK_LINK)
        soup = BeautifulSoup(r.text, 'html.parser')
        csrf = soup.select_one("[name='csrf-token']")['content']
        s.headers['x-csrf-token'] = csrf
        s.headers['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        r = s.post(CHARTINK_SCAN_URL, data=payload)

        df = pd.DataFrame()

        for item in r.json()['data']:
            df = pd.concat([df, pd.DataFrame([item])], ignore_index=True)

    return df