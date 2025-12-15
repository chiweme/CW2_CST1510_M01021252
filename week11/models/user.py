import bcrypt

class User:
    """
    Represents a system user stored in the database."""
    
    def __init__(self, username: str, password_hash: str, role: str):
        #private attributes
        self._username = username
        self._password_hash = password_hash
        self._role = role
    
    def __repr__(self):
        return f"User(username='{self.username}', role='{self.role}')"
    
    #getters read only access
    
        
    def get_username(self) -> str:
        return self._username
    
   
    def get_password_hash(self) -> str:
        return self._password_hash
    
   
    def get_role(self) -> str:
        return self._role
    
    #mutators
    def set_role(self, new_role: str):
        """Update the user's role."""
        self._role = new_role
    
    
    #object display representation
    def __str__(self):
        return f"User(username={self._username}, role={self._role})"
    
    
    