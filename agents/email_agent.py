import json
from config import DATA_PATH

def load_emails():
    with open(f"{DATA_PATH}/emails.json", "r", encoding="utf-8") as f:
        return json.load(f)

def format_emails():
    emails = load_emails()
    return "\n".join([f"From: {e['from']}, Subject: {e['subject']}, Date: {e['date']}" for e in emails])
