import bcrypt
import os
#File for week 7 user storage
USER_DATA_FILE = "users.txt"

#password hashing
def hash_password(password: str) -> str:
    """Hash a plaintext password using bcrypt.
    Returns:
        str: the hashed password (UTF-8 decoded).
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")

#password verification
def verify_password(password: str, hashed: str) -> bool:
    """Verify that a plaintext password matches the stored hash.
    Returns:
        bool: true if paassword matches the hash, False otherwise.
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))

#check if username exists
def user_exists(username: str) -> bool:
    """Check if the username already exists inside users.txt.
    each line in users.txt has 3 values:
        username, password_hash, role
    Returns:
        bool: true if username exists, False otherwise.
    """
    if not os.path.exists(USER_DATA_FILE):
        return False
    
    with open(USER_DATA_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) >= 1:
                stored_username = parts[0]
                if stored_username == username:
                    return True
    return False 


def save_user(username: str, password_hash: str, role: str):
    """Save a new user to the users.txt file.
    format stored:
        username,hashedpassword,role
    """
    with open(USER_DATA_FILE, "a") as file:
        file.write(f"{username},{password_hash}\n")


def validate_username(username: str):
    """Check if a username meets length + rules.
    Returns:
        (bool, str): (is_valid, error_message)
    """
    if not (3 <= len(username) <= 20):
        return False, "Username must be 3-20 characters long."
    if not username.isalnum():
        return False, "Username must be alphanumeric only."
    return True, ""

def validate_password(password):
    """
    Basic password rule:
            - at least 6 characters
    Returns:
        (bool, str): (is_valid, error_message)
    """
    if len(password) < 6:
        return False, "Password must at least be 6 characters long."
    return True, ""


#register a new user
def register_user(username: str, password: str, role: str):
    """Register a new user with a username, hashed password, and role.
    Returns:
        bool: true if registration successful, False otherwise.
    """
    #prevent duplicates
    if user_exists(username):
        print(f"Error: Username '{username}' already exists.")
        return False
    
    hashed = hash_password(password)
    save_user(username, hashed, role)
    return True 
    

#login user
def login_user(username: str, password: str):
    """Attempt to log in a user.
    Returns:
        (bool, role):
            True + role - login successful
            False + None - login failed
    """
    if not os.path.exists(USER_DATA_FILE):
        return False, None
    
    with open(USER_DATA_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            
            #must contain exactly 3 values
            if len(parts) != 3:
                continue
            
            stored_username, stored_hash, role = parts
            
            if stored_username == username and verify_password(password, stored_hash):
                return True, role
            
    return False, None   

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
                password = input("Password: ").strip()
                role = input("Role (cyber/data/it): ").strip().lower()
                
                if register_user(username, password, role):
                    print("User registered successfully!")
                else:
                    print("Error: Username already exists.")
                      
        
            elif choice == "2":
                print("\n--- USER LOGIN ---")
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                
                success, role = login_user(username, password)
                if success:
                    print(f"Logged in as {username} ({role}).")
                else:
                    print("Invalid username or password.")
    
            elif choice == "3":
                print("Exiting. Goodbye!")
                break
        
            else:
                print("Error: Invalid option. Try again.")
       
if __name__ == "__main__":
 main()

