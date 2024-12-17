import random
import string
import json
import os

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to save a password
def save_password(account, password, file="passwords.json"):
    passwords = {}
    
    # Load existing passwords if the file exists
    if os.path.exists(file):
        with open(file, "r") as f:
            passwords = json.load(f)
    
    # Add new password
    passwords[account] = password
    
    # Save to file
    with open(file, "w") as f:
        json.dump(passwords, f, indent=4)
    print(f"Password saved for account: {account}")

# Function to retrieve a password
def retrieve_password(account, file="passwords.json"):
    if os.path.exists(file):
        with open(file, "r") as f:
            passwords = json.load(f)
        return passwords.get(account, "Account not found.")
    else:
        return "No saved passwords found."

# Main menu
def password_manager():
    print("=== Password Generator and Manager ===")
    print("1. Generate a new password")
    print("2. Save a password")
    print("3. Retrieve a password")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            length = int(input("Enter password length (default is 12): ") or 12)
            new_password = generate_password(length)
            print(f"Generated Password: {new_password}")
        
        elif choice == "2":
            account = input("Enter the account name: ")
            password = input("Enter the password (or press Enter to generate one): ")
            if not password:
                password = generate_password()
                print(f"Generated Password: {password}")
            save_password(account, password)
        
        elif choice == "3":
            account = input("Enter the account name to retrieve the password: ")
            result = retrieve_password(account)
            print(f"Password for {account}: {result}")
        
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    password_manager()
