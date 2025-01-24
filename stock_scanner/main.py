# chartink_alerts/main.py
from datetime import datetime
from .config import CHARTINK_CONDITION
from .stock_scan import GetDataFromChartink
from .alert_manager import send_telegram_alert, load_alerts, save_alerts

def main():
    # Load previously sent alerts
    alerts_sent = load_alerts()
    today = datetime.now().strftime("%Y-%m-%d")
    if today not in alerts_sent:
        alerts_sent[today] = []

    # Get stock data from Chartink
    data = GetDataFromChartink(CHARTINK_CONDITION)
    data = data.sort_values(by='per_chg', ascending=False)

    # Process each stock and send alerts for new ones
    for index, row in data.iterrows():
        nsecode = row['nsecode']
        if nsecode not in alerts_sent[today]:
            # Prepare alert message
            message = (
                f"Stock Alert:\n"
                f"Name: {row['name']}\n"
                f"NSE Code: {row['nsecode']}\n"
                f"Close Price: {row['close']}\n"
                f"Percentage Change: {row['per_chg']}%\n"
                f"Volume: {row['volume']}\n"
            )

            send_telegram_alert(message)

            # Mark stock as alerted
            alerts_sent[today].append(nsecode)

    print(data)

    # Save updated alerts
    save_alerts(alerts_sent)

if __name__ == "__main__":
    main()
