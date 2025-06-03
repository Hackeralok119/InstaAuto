def run_likes():
    from utils.session import load_accounts
    accounts = load_accounts()
    link = input("Enter Post Link: ")
    print(f"Liking post from {len(accounts)} accounts...")
    # Add like logic here
