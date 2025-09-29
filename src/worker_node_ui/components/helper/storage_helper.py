import json, os

SESSION_FILE = "user_session.json"

def save_session(user_data: dict):
    with open(SESSION_FILE, "w") as f:
        json.dump(user_data, f)

def load_session() -> dict:
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as f:
            return json.load(f)
    return {}

def clear_session():
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
