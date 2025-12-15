from week11.models.dataset import Dataset

class DatasetService:
    """CRUD for Dataset objects stored in memory."""
    
    def __init__(self):
        self.datasets = []
        
    #create
    def add(self, dataset: Dataset):
        self.datasets.append(dataset)
        
    #read
    def get_all(self):
        return self.datasets
    
    def get_by_name(self, name: str):
        for ds in self.datasets:
            if ds.name == name:
                return ds
        return None
    
    #update
    def update_description(self, name: str, new_description: str):
        ds = self.get_by_name(name)
        if ds:
            ds.update_description(new_description)
            return True
        return False
    
    #delete
    def delete(self, name: str):
        self.datasets = [ds for ds in self.datasets if ds.name != name]
        