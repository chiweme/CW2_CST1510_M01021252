class ITTicket:
    """Represents an IT helpdesk ticket from the it_tickets table."""
    
    def __init__(self, title: str, assigned_to: str, date_created: str,
                 status: str, resolution_time: int):
        self._title = title
        self._assigned_to = assigned_to
        self._date_created = date_created
        self._status = status
        self._resolution_time = resolution_time
        
    def __repr__(self):
        #tiket_id not implemented; using title for debugging
        return f"ITTicket(title='{self._title}', status='{self._status}')"
    
    #getters
    def get_title(self) -> str:
        return self._title 
        
    def get_assigned_to(self) -> str:
        return self._assigned_to
        
    def get_date_created(self) -> str:
        return self._date_created
        
    def get_status(self) -> str:
            return self._status
        
    def get_resolution_time(self) -> int:
        return self._resolution_time
        
    #mutators
    def update_status(self, new_status: str):
        """update status (open, close, in-progress)."""
        self._status = new_status
    def update_resolution_time(self, new_time: int):
        """update the resolution time after closing."""
        self._resolution_time = new_time 
    #display
    def __str__(self):
        return f"ITTicket(title={self._title}, status={self._status}, assigned_to={self._assigned_to})"
    