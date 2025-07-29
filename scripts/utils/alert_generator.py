# scripts/utils/alert_generator.py

import smtplib
from email.mime.text import MIMEText
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json
import csv
import os
from datetime import datetime

# ========== CONFIG ==========
SLACK_TOKEN = os.getenv("SLACK_TOKEN", "xoxb-your-slack-token")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL", "#alerts")

EMAIL_FROM = os.getenv("EMAIL_FROM", "alertbot@example.com")
EMAIL_TO = os.getenv("EMAIL_TO", "you@example.com")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_PASS = os.getenv("SMTP_PASS", "your-email-password")

CSV_FILE = "alerts.csv"
JSON_FILE = "alerts.json"

# ========== SLACK ALERT ==========
def send_slack_alert(message):
    client = WebClient(token=SLACK_TOKEN)
    try:
        client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
    except SlackApiError as e:
        print(f"[!] Slack error: {e.response['error']}")

# ========== EMAIL ALERT ==========
def send_email_alert(subject, body):
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL_FROM
        msg["To"] = EMAIL_TO
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_FROM, SMTP_PASS)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"[!] Email error: {e}")

# ========== FILE EXPORT ==========
def export_to_csv(alert_data):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=alert_data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(alert_data)

def export_to_json(alert_data):
    with open(JSON_FILE, 'a') as f:
        json.dump(alert_data, f)
        f.write("\n")

# ========== COMBINED ALERT ==========
def trigger_alert(event, source_ip, raw_log):
    timestamp = datetime.now().isoformat()
    alert = {
        "time": timestamp,
        "event": event,
        "source_ip": source_ip,
        "raw": raw_log.strip()
    }

    msg = f"[{alert['time']}] {event} from {source_ip}"

    print(msg)
    send_email_alert(f"SECURITY ALERT: {event}", msg)
    send_slack_alert(msg)
    export_to_csv(alert)
    export_to_json(alert)

#To use anywhere 
#from scripts.utils.alert_generator import trigger_alert

# Example usage inside a log parser
#trigger_alert("Failed SSH Login", "192.168.1.77", "Failed password for invalid user root from 192.168.1.77 port 22 ssh2")

