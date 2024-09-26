# src/utilities/data_processing.py

import pandas as pd

def save_data_to_csv(data, filename):
    df = pd.DataFrame(data, columns=["Crack Location"])
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
