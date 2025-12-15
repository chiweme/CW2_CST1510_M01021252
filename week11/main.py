#import all model classes 
from models.user import User
from models.security_incident import SecurityIncident
from models.dataset import Dataset
from models.it_ticket import ITTicket 

from services.incident_service import IncidentService 
from services.dataset_service import DatasetService 
from services.ticket_service import TicketService 

#object creation 
def create_sample_objects():
    """creates example objects for all four domains."""
    
    users = [
        User("athena", "hash123", "cyber"),
        User("max", "hash456", "data"),
        User("thalia", "hash789", "it")
    ]
    
    incidents = [
        SecurityIncident(1, "Phishing Spike", "High", "2025-11-27",
                         "multiple phishing emails detected.", "open"),
        SecurityIncident(2, "Randsomware Attempt", "Critical", "2025-11-20",
                         "Suspicious encryption behaviour detected.", "Investigating")
    ]
    
    datasets = [
        Dataset("Sales Data", 5000, 11, "Retail performance dataset."),
        Dataset("Customer Logs", 12000, 18, "Behaviour analytics dataset.")
    ]
    
    tickets = [
        ITTicket("Laptop not booting", "Bob", "2025-11-22",
                 "open", 0),
        ITTicket("VPN not connecting", "Alice", "2025-11-25",
                 "open", 0)
    ]
    
    return users, incidents, datasets, tickets
    
    
#Display Helpers
def print_list(items: list):
    """Prints each object in a list using its __str__ method."""
    for item in items:
        print(" -", item)
        
#CRUD DEMO
def demonstrate_crud(users, incidents, datasets, tickets):
    """Demonstrates Create, Read, Update, Delete
    for all OOP model objects."""
    
    print("\n" + "=" * 50)
    print("INITIAL OBJECTS")
    print("=" * 50)
    
    print("\n" + "=" * 50)
    print("Users")
    print("=" * 50)
    print_list(users)
    
    #initial incidents 
    print("\n" + "=" * 50)
    print("Security Incidents")
    print("=" * 50)
    print_list(incidents)
    
    #initial datasets
    print("\n" + "=" * 50)
    print("Datasets")
    print("=" * 50)
    print_list(datasets)
    
    print("\n" + "=" * 50)
    print("IT Tickets")
    print("=" * 50)
    print_list(tickets)
    
    #Update
    print("\n" + "=" * 50)
    print("UPDATES (Mutator Methods)")
    print("=" * 50)
    
    #Update user role
    users[0].set_role("admin")
    
    #update incident status
    incidents[0].update_status("Closed")
    
    #update ticket 
    tickets[0].update_status("closed")
    
    print_list(users)
    print_list(incidents)
    print_list(datasets)
    print_list(tickets)
    
    #Create
    print("\n" + "=" * 50)
    print("ADDING NEW OBJECTS")
    print("=" * 50)
    
    new_incident = SecurityIncident(
        3, "Suspicious Login Attempt", "Medium", "2025-11-28",
        "Unusual login from foreign IP.", "Open"
    )
    incidents.append(new_incident)
    print_list(incidents)
    
    #Delete
    print("\n" + "=" * 50)
    print("DELETING AN OBJECT")
    print("=" * 50)
    
    deleted_ticket = tickets.pop(1)
    print("Deleted ticket:", deleted_ticket)
    
    print("\nRemaining Tickets:")
    print_list(tickets)
    
#Main
def main():
    print("\n" + "=" * 50)
    print("WEEK 11 OOP MODEL DEMOSTRATION")
    print("=" * 50)    
        
    #create example objects
    users, incidents, datasets, tickets = create_sample_objects()
    demonstrate_crud(users, incidents, datasets, tickets)
    
        
if __name__ == "__main__":
    main()    