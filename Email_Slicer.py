def email_slicer(email):
    """
    Function to slice the email into username and domain.
    """
    try:
        username, domain = email.split('@')
        return username, domain
    except ValueError:
        print("Invalid email format. Please ensure the email contains one '@' symbol.")
        return None, None

def main():
    """
    Main function to run the email slicer.
    """
    print("Welcome to the Email Slicer!")
    email = input("Please enter your email address: ").strip()
    
    username, domain = email_slicer(email)
    
    if username and domain:
        print(f"Username: {username}")
        print(f"Domain: {domain}")

if __name__ == "__main__":
    main()
