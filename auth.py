import bcrypt
import os
#File for week 7 user storage
USER_DATA_FILE = "users.txt"

#password hashing
def hash_password(password: str) -> str:
    """Hash a plaintext password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")

#password verification
def verify_password(password: str, hashed: str) -> bool:
    """Verify that a plaintext password matches the stored hash."""
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))

#check if username exists
def user_exists(username):
    """Check if the username already exists inside users.txt."""
    if not os.path.exists(USER_DATA_FILE):
        return False
    
    with open(USER_DATA_FILE, "r") as file:
        for line in file:
            stored_username, _ = line.strip().split(",")
            if stored_username == username:
                return True
            
    return False

def save_user(username, password_hash):
    """Save a new user to the users.txt file."""
    with open(USER_DATA_FILE, "a") as file:
        file.write(f"{username},{password_hash}\n")

def validate_username(username):
    if not (3 <= len(username) <= 20):
        return False, "Username must be 3-20 characters long."
    if not username.isalnum():
        return False, "Username must be alphanumeric only."
    return True, ""

def validate_password(password):
    if len(password) < 6:
        return False, "Password must at least be 6 characters long."
    return True, ""


#register a new user
def register_user(username, password):
    """Register a new user for week 7 file-based authentication."""
    if user_exists(username):
        print(f"Error: Username '{username}' already exists.")
        return False
    
    hashed = hash_password(password)
    save_user(username, hashed)
    print(f"Success: User '{username}' registered successfully!")
    return True

#login user
def login_user(username, password):
    """Validate login using users.txt"""
    if not os.path.exists(USER_DATA_FILE):
        print("Error: No users registered yet.")
        return False
    
    with open(USER_DATA_FILE, "r") as file:
        for line in file:
            stored_username, stored_hash = line.strip().split(",")
            if stored_username == username:
                if verify_password(password, stored_hash):
                    print(f"Success: Welcome, {username}!")
                    return True
                else:
                    print("Error; Invalid password.")
                    return False
            
    print("Error: Username not found.")
    return False

#CLI Menu (Week 7 only)
def display_menu():
    """Displays the main menu options."""
    print("\n" + "="*50)
    print(" MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print(" Secure Authentication System")
    print("="*50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-"*50)
    
    
def main():
    """Main program loop."""
    print("\nWelcome to the Week 7 Authentication System!")

    while True:
        display_menu()
        choice = input("\nPlease select an option (1-3): ").strip()

        if choice == '1':
            # Registration flow
            print("\n--- USER REGISTRATION ---")
            username = input("Enter a username: ").strip()
            
            if choice == "1":
                print("\n--- USER REGISTRATION ---")
                username = input("Enter a username: ").strip()
                valid, msg = validate_username(username)
                if not valid:
                    print("Error:", msg)
                    continue

        
                password = input("Enter a password: ").strip()
                # Validate password
                valid, msg = validate_password(password)
                if not valid:
                    print(f"Error:", msg)
                    continue

                # Confirm password
                password_confirm = input("Confirm password: ").strip()
                if password != password_confirm:
                    print("Error: Passwords do not match.")
                    continue

                # Register the user
                register_user(username, password)
        
        elif choice == "2":
            print("\n--- USER LOGIN ---")
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            login_user(username, password)
    
        elif choice == "3":
            print("Exiting. Goodbye!")
            break
        
        else:
            print("Error: Invalid option.")
       
if __name__ == "__main__":
 main()

