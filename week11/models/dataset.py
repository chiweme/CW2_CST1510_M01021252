class Dataset:
    """represents a dataset stored in the datasets table."""
    
    def __init__(self, name: str, rows: int, columns: int, description: str):
        self._name = name
        self._rows = rows
        self._columns = columns
        self._description = description
        
    def __repr__(self):
        return f"Dataset(name='{self.name}', rows={self.rows})"
    
    #getters
    def get_name(self) -> str:
        return self._name
    
    def get_rows(self) -> int:
        return self._rows
    
    def get_columns(self) -> int:
        return self._columns
    
    def get_description(self) -> str:
        return self._description
    
    #mutators 
    def update_description(self, new_description: str):
        """update the dataset description."""
        self._description = new_description
        
    #display
    def __str__(self):
        return f"Dataset(name={self._name}, rows={self._rows}, columns={self._columns})"
    