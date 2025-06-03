

import requests, uuid, secrets, json
from getpass import getpass

def login_account():
    username = input("Enter Instagram Username: ")
    password = getpass("Enter Instagram Password: ")
    device_id = f"android-{secrets.token_hex(8)}"

    data = {
        'username': username,
        'password': password,
        'device_id': device_id,
        '_csrftoken': 'missing',
        'phone_id': str(uuid.uuid4()),
        'guid': str(uuid.uuid4()),
        'login_attempt_count': 0
    }

    headers = {
        'User-Agent': "Instagram 113.0.0.39.122 Android",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
    }

    r = requests.post('https://b.i.instagram.com/api/v1/accounts/login/', data=data, headers=headers)
    
    if "logged_in_user" in r.text:
        session_id = r.cookies.get('sessionid')
        ds_user_id = r.cookies.get('ds_user_id')

        # Save to accounts.json
        try:
            with open("accounts.json", "r") as f:
                accs = json.load(f)
        except:
            accs = []

        accs.append({
            "username": username,
            "sessionid": session_id,
            "ds_user_id": ds_user_id
        })

        with open("accounts.json", "w") as f:
            json.dump(accs, f, indent=2)

        print(f"Login success: {username}")
    else:
        print("Login failed. Try again.")
        