from typing import Literal
from sklearn.preprocessing import MinMaxScaler,StandardScaler
import pandas as pd
import numpy as np

def normalize_data(df:pd.DataFrame, method:Literal["minmax","standard"], columns=None):
    df_copy = df.copy()
    if columns is None:
        columns = df_copy.select_dtypes(include=np.number).columns
    if method=='minmax':
        scaler = MinMaxScaler()
    else:
        scaler = StandardScaler()
    df_copy[columns] = scaler.fit_transform(df_copy[columns])
    return df_copy

def filling_missing_mean(df:pd.DataFrame,columns=None):
    df_copy = df.copy()
    if columns is None:
        columns = df_copy.select_dtypes(include=np.number).columns
    for col in columns:
        df_copy[col] = df_copy[col].fillna(df_copy[col].mean())
    return df_copy

def drop_missing(df:pd.DataFrame,columns=None,threshold=None):
    df_copy = df.copy()
    if columns is not None:
        return df_copy.dropna(subset=columns)
    if threshold is not None:
        return df_copy.dropna(thresh=int(threshold*df_copy.shape[1]))
    return df_copy.dropna()