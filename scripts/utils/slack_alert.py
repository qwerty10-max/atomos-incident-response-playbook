# scripts/utils/slack_alert.py

import json
import requests

# ========== CONFIG ==========
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/XXX/YYY/ZZZ"  # <-- Replace with your real webhook

# ========== SEND ALERT ==========
def send_slack_alert(message, alert_type="info"):
    emoji_map = {
        "info": "🔍",
        "warning": "⚠️",
        "critical": "🚨"
    }

    emoji = emoji_map.get(alert_type, "🔍")

    payload = {
        "text": f"{emoji} *SIEM Alert:* {message}"
    }

    try:
        response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        if response.status_code != 200:
            print(f"[!] Slack alert failed: {response.text}")
    except Exception as e:
        print(f"[!] Error sending Slack alert: {e}")

# ========== TEST ==========
if __name__ == "__main__":
    send_slack_alert("Suspicious login attempt detected from 10.10.10.5", "warning")

# Usage in Log Alerting Flow
#In alert_generator.py or log_analysis.py:
#from scripts.utils.slack_alert import send_slack_alert
#send_slack_alert(f"Malware detected in logs: {log_path}", alert_type="critical")
