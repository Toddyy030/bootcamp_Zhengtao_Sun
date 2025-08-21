import pandas as pd
import yfinance as yf
from typing import Literal
import requests
from dotenv import load_dotenv
import os
from pathlib import Path

def subtract_columns(df:pd.DataFrame,column1:str,column2:str):
    result = df[column1] - df[column2]
    return result
    
def daily_tickerFetcher(symbol: str,start:str,end:str) -> pd.DataFrame:
    try:
        df_api = yf.download(tickers=symbol,start=start,end=end,auto_adjust=False)
        if isinstance(df_api.columns, pd.MultiIndex):
            df_api.columns = df_api.columns.droplevel(1)
        df_api = df_api.reset_index()
        df_api.rename(columns={"Open":"open","High":"high","Low":"low","Close":"close","Volume":"volume","Adj Close":"adj close","Date":"date"},
                      inplace=True)
        df_api["ticker"] = symbol
        print("loading data from yfinance is successful")
    except:
        load_dotenv()
        api_key = os.getenv("API_KEY")
        url = "https://www.alphavantage.co/query"
        params = {
        "function":"TIME_SERIES_DAILY",
        "symbol":symbol,
        "outsize":"full",
        "data_type":"json",
        "apikey":api_key
        }
        r = requests.get(url=url,params=params)
        js = r.json()
        js.keys()
        series = js["Time Series (Daily)"]
        df_api = pd.DataFrame(series).T.rename_axis("date").reset_index()
        df_api["date"] = pd.to_datetime(df_api["date"])
        df_api.rename(columns={"1. open":"open","2. high":"high","3. low":"low","4. close":"close","5. volume":"volume"},inplace=True)
        for column in df_api.columns[1:]:
            df_api[column] = pd.to_numeric(df_api[column])
        df_api = df_api.sort_values("date").set_index("date")
        df_api = df_api.loc[start:end]
        df_api = df_api.reset_index()
        print("loading data from alpha vantage API is successful")
    return df_api

def detect_format(path:str):
    s = str(path).lower()
    if s.endswith(".csv"):
        return "csv"
    elif s.endswith(".parquet") or s.endswith('.pq') or s.endswith('.parq'):
        return "parquet"
    
def read_df(path:str):
    p = Path(path)
    format = detect_format(p)
    if format == "csv":
        return pd.read_csv(p)
    elif format == "parquet":
        try:
            return pd.read_parquet(p)
        except Exception as e:
            raise RuntimeError('Parquet engine not available. Install pyarrow or fastparquet.') from e
