def run_comment():
    from utils.session import load_accounts
    accounts = load_accounts()
    link = input("Enter Post Link: ")
    comment = input("Enter Comment Text: ")
    print(f"Commenting on post with {len(accounts)} accounts...")
    # Add comment logic here
