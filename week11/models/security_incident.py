class SecurityIncident:
    """represents a security incident stored in the security_incidents table."""
    
    def __init__(self, incident_id: int, title: str, severity: str, date_reported: str,
                 description: str, status: str):
        self._incident_id = incident_id 
        self._title = title 
        self._severity = severity
        self._date_reported = date_reported
        self._description = description
        self._status = status
        
    #properties
    @property
    def incident_id(self):
        return self._incident_id
    
    @property
    def title(self):
        return self._title
    
    @property
    def severity(self):
        return self._severity
    
    @property 
    def date_reported(self):
        return self._date_reported
    
    @property
    def description(self):
        return self._description
    
    @property
    def status(self):
        return self._status 
     
    
    #getters 
    def get_title(self) -> str:
        return self._title 
        
    def get_severity(self) -> str:
        return self._severity
        
    def get_date_reported(self) -> str:
        return self._date_reported
        
    def get_description(self) -> str:
        return self._description
        
    def get_status(self) -> str:
        return self._status
        
    #mutators
    def update_status(self, new_status: str):
        """update the incident's status (open, closed, investigating)."""
        self._status = new_status
            
    def __str__(self):
        return f"SecurityIncident(title={self._title}, severity={self._severity}, status={self._status})"
    
    #representation for printing/debugging    
    def __repr__(self):
        return f"SecurityIncident(id={self._incident_id}, severity={self.severity}, title='{self._title}')"
    
    