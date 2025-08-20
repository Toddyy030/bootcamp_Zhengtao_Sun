import pandas as pd

def subtract_columns(df:pd.DataFrame,column1:pd.Series,column2:pd.Series):
    result = df[column1] - df[column2]
    return result
    