import json
from config import DATA_PATH

def load_tasks():
    with open(f"{DATA_PATH}/tasks.json", "r", encoding="utf-8") as f:
        return json.load(f)

def format_tasks():
    tasks = load_tasks()
    return "\n".join([f"{t['task']} by {t['deadline']}" for t in tasks])
