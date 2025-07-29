#!/usr/bin/env python3

import re
import json
import csv
import smtplib
from email.mime.text import MIMEText
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

# Configs
LOG_FILE = "/var/log/auth.log"
CSV_FILE = "alerts.csv"
JSON_FILE = "alerts.json"
SLACK_TOKEN = "xoxb-your-slack-bot-token"
SLACK_CHANNEL = "#alerts"
EMAIL_FROM = "alertbot@example.com"
EMAIL_TO = "your@email.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_PASS = "your-email-password"

PATTERNS = {
    "Failed SSH Login": r"Failed password for (invalid user )?.* from (\d{1,3}(?:\.\d{1,3}){3})",
    "Successful SSH Login": r"Accepted password for .* from (\d{1,3}(?:\.\d{1,3}){3})",
    "Sudo Abuse": r"sudo: .* : TTY=.* ; PWD=.* ; USER=root ; COMMAND=.*",
    "User Enumeration": r"Invalid user .* from (\d{1,3}(?:\.\d{1,3}){3})"
}

# Initialize Slack client
slack_client = WebClient(token=SLACK_TOKEN)

# Email alert
def send_email(subject, body):
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

# Slack alert
def send_slack(message):
    try:
        slack_client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
    except SlackApiError as e:
        print(f"[!] Slack error: {e.response['error']}")

# Write to CSV/JSON
def write_output(alert):
    with open(CSV_FILE, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=alert.keys())
        writer.writerow(alert)
    with open(JSON_FILE, 'a') as jsonfile:
        json.dump(alert, jsonfile)
        jsonfile.write('\n')

# Extract timestamp from line
def extract_timestamp(log_line):
    try:
        raw = " ".join(log_line.split()[:3])
        return datetime.strptime(raw, "%b %d %H:%M:%S").replace(year=datetime.now().year).isoformat()
    except:
        return datetime.now().isoformat()

# Core logic
def analyze_line(line):
    for label, pattern in PATTERNS.items():
        match = re.search(pattern, line)
        if match:
            timestamp = extract_timestamp(line)
            src_ip = match.groups()[-1] if match.groups() else "Unknown"
            alert = {
                "time": timestamp,
                "event": label,
                "source_ip": src_ip,
                "raw": line.strip()
            }
            alert_text = f"[{alert['time']}] {alert['event']} from {alert['source_ip']}"
            print(alert_text)
            send_email(f"SECURITY ALERT: {label}", alert_text)
            send_slack(alert_text)
            write_output(alert)

# Real-time watcher
class LogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == LOG_FILE:
            with open(LOG_FILE, 'r') as file:
                lines = file.readlines()[-20:]  # tail last 20 lines
                for line in lines:
                    analyze_line(line)

def start_monitor():
    print(f"[*] Monitoring {LOG_FILE} in real-time...")
    observer = Observer()
    observer.schedule(LogHandler(), path=LOG_FILE, recursive=False)
    observer.start()
    try:
        while True:
            pass  # Keep alive
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_monitor()

