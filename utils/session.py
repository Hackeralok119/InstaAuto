import json

def load_accounts():
    try:
        with open("accounts.json", "r") as f:
            return json.load(f)
    except:
        return []
        