## Problem Statement
Excess return is a valuable trading signal for portfolio constructions and stock selection in quantitative stock investing. Predicting stocks’ future excess return allows portfolio managers to make informed decisions ahead of time, and improve portfolio strategies. This project aims to leverage reliable historical stock data (OHLCV) and benchmarks in the past 5 years from public open API like yfinance and Alpha vantage, and construct factors like momentum factors and value factors. We will use machine learning regression models as the tool predicts one day ahead excess return. Model performance will be evaluated through backtesting, and deliver actionable insights to help portfolio managers to construct strategies with stable 
return. 
## Project Structure
- /data/:All the data required for analysis store in this folder; /data/raw: all the unprocessed data which directly fetch from API store in this folder; /data/processed: all the data after cleaning or normalize or feature engineering store in this folder
- /notebooks/: this folder only contains .ipynb files. This folder demonstrate the process of analyzing data
- /src/:this folders contains all the reusable functions
- /docs/: this folder demonstrate all the information stakeholders need to know
## Data Storage
- **data folder structure**: ./data/raw, ./data/processed<br>
- **file format**: .csv, .parquet<br>
- **method to read data files**: construct read_df() function to read .csv and .parquet files. See more details in ./src/utils.py