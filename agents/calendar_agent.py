import json
from config import DATA_PATH

def load_calendar():
    with open(f"{DATA_PATH}/calendar.json", "r", encoding="utf-8") as f:
        return json.load(f)

def format_calendar():
    events = load_calendar()
    return "\n".join([f"{c['title']} at {c['time']} on {c['date']}" for c in events])
