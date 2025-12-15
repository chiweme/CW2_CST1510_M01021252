import pandas as pd
import os
#absolute path to the shared data directory (one level above this file)
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))

def load_excel(filename):
    """Load an excel file from the projects/data directory.
    Args: 
        filename (str): name of the excel file 
    Returns: 
        pd.DataFrame: loaded excel data as a pandas DataFrame
    Raises:
        FileNotFoundError: if the file does not exist in the data directory"""
    path = os.path.join(DATA_DIR, filename)
    #validate file existance before loading
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    
    return pd.read_excel(path)

