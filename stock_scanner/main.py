from datetime import datetime
from .config import CHARTINK_CONDITION
from .stock_scan import GetDataFromChartink
from .alert_manager import send_telegram_alert, load_alerts, save_alerts

def main():

    alerts_sent = load_alerts()
    alert_failed = []
    data = GetDataFromChartink(CHARTINK_CONDITION)
    data = data.sort_values(by='per_chg', ascending=False)

    for index, row in data.iterrows():
        nsecode = row['nsecode']
        if nsecode not in alerts_sent:

            message = (
                f"<b>Stock Alert:</b> {datetime.now().time()}\n"
                f"<b>Name:</b> {row['name']}\n\n"
                f"<b>NSE Code:</b> <em>{row['nsecode']}</em>\n"
                f"<b>Close Price:</b> <em>{row['close']}</em>\n\n"
                f"<b>Percentage Change:</b> {row['per_chg']}%\n"
                f"<b>Volume:</b> {row['volume']}\n"
            )

            isSuccess = send_telegram_alert(message)

            if isSuccess:
                alerts_sent.append(nsecode)
            else:
                alert_failed.append(nsecode)

    print(data)
    save_alerts(alerts_sent, alert_failed)

if __name__ == "__main__":
    main()
