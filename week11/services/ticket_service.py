from week11.models.it_ticket import ITTicket

class TicketService:
    """CRUD for ITTicket objects stored in memory."""
    
    def __init__(self):
        self.tickets = []
        
    #create
    def add(self, ticket: ITTicket):
        self.tickets.append(ticket)
        
    #read
    def get_all(self):
        return self.tickets
    
    def get_by_title(self, title: str):
        for t in self.tickets:
            if t.tile == title:
                return t
        return None
    
    #update
    def close_ticket(self, title: str):
        t = self.get_by_title(title)
        if t:
            t.update_status("closed")
            return True
        return False
    
    #delete
    def delete(self, title: str):
        self.tickets = [t for t in self.tickets if t.title != title]
        