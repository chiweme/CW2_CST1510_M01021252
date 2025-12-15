from week11.models.security_incident import SecurityIncident

class IncidentService:
    """CRUD manager for SecurityIncident objects (in-memory)."""
    
    def __init__(self):
        self.incidents = [] #internal list of incidents 
        
        #create
        def add(self, incident: SecurityIncident):
            self.incidents.append(incident)
            
        #read
        def get_all(self):
            return self.incidents
        
        def get_by_id(self, incident_id: int):
            for inc in self.incidents:
                if inc.incident_id == incident_id:
                    return inc
                return None
            
        #update
        def update_status(self, incident_id: int, new_status: str):
            inc = self.get_by_id(incident_id)
            if inc:
                inc.update_status(new_status)
                return True
            return False
        
        #delete
        def delete(self, incident_id: int):
            self.incidents = [
                inc for inc in self.incidents if inc.incident_id != incident_id
            ]
            