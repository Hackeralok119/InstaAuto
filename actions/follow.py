def run_follow():
    from utils.session import load_accounts
    accounts = load_accounts()
    user = input("Enter Username to Follow: ")
    print(f"Following {user} from {len(accounts)} accounts...")
    # Add follow logic here
    