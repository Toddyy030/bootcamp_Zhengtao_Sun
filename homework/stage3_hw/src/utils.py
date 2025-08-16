import pandas as pd

def get_summary_stat(df:pd.DataFrame) -> pd.DataFrame:
    summary = df.describe()
    return summary

def get_mean_value(df:pd.DataFrame):
    try:
        mean = df["value"].mean()
        return mean
    except Exception as e:
        print("Error occur: ",e)