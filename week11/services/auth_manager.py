import bcrypt 
from week11.services.database_manager import DatabaseService 
from week11.models.user import User 

class AuthService:
    """
    Handles:
    - password hashing
    - login verification
    - registration
    - role checking
    Uses DatabaseService for DB access.
    
    """
    
    def __init__(self, database_manager: DatabaseService):
        self.db = database_manager 
        
    #password security
    def hash_password(self, password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    def verify_password(self, plain, hashed):
        return bcrypt.checkpw(plain.encode(), hashed.encode())
    
    #login
    def login(self, username, password):
        user: User = self.db.get_user(username)
        if not user:
            return False, None #no such user
        
        if self.verify_password(password, user.get_password_hash()):
            return True, user.get_role()
        
        return False, None #wrong password
    
    def get_role(self):
        return self._role 
    
    
    #register
    def register(self, username, password, role):
        #check if user exists
        if self.db.get_user(username):
            return False, "Username already exists."
        
        hashed = self.hash_password(password)
        ok = self.db.insert_user(username, hashed, role)
        
        if ok:
            return True, "User registered successfully"
        return False, "Database error while registering user."
    
    