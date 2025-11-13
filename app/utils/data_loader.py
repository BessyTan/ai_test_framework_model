import pandas as pd
import os

DATA_DIR = "data"
DEFAULT_FILE = "sample.csv"

def load_data(file_path=None):
    """Load CSV data into a DataFrame"""
    if file_path is None:
        file_path = os.path.join(DATA_DIR, DEFAULT_FILE)
    return pd.read_csv(file_path)