import pandas as pd

def describe() -> pd.DataFrame:
    df = pd.read_csv("data/statistics-macon.csv")
    filtered = df[df.crime.notna()]
    return filtered.describe()
