import pandas as pd
from cohere.types import ToolV2, ToolV2Function

def describe() -> pd.DataFrame:
    df = pd.read_csv("data/statistics-macon.csv")
    filtered = df[df.crime.notna()]
    return filtered.describe()

describe_tool = ToolV2(
        type="function",
        function=ToolV2Function(
            name="describe_macon_statistics",
            description="Returns descriptive statistics of crime data for Macon.",
            parameters={}
        )
    )