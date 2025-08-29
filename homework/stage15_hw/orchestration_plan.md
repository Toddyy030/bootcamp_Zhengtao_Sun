## Orchestration Plan
## Jobs & tasks in this project
- Ingest: fetch S&P500 stock data(OHLCV) from public API yfinance and alpha vantage
- clean: using clean stratgy like filling missing values using mean/median, removing outliers by applying IQR(Q3-Q1,[ Q1 − 1.5×IQR , Q3 + 1.5×IQR ]), z-score, or winsorize
- model: applying feature engineering to investigate relevant features with targers. leveraging time series model and linear regression to predict how selected features fit the target next-day excess return
- report: deliver plot comparing prediction vs truth and inform assumption, risks and limitations to stakeholders
## Order/dependencies
- ingest --> clean --> train --> report
## logging & checkpoints strategy
| task           | log_messages                  | checkpoint_artifact |
|----------------|-------------------------------|---------------------|
| ingest         | start/end, rows, source URI   | prices_raw.json     |
| clean          | start/end, rows in/out        | prices_clean.json   |
| train_or_score | params, metrics               | model.json          |
| report         | artifact path                 | report.txt          |
## Right-sizing automation
- automate: ingest latest data, clean data, feature engineering, and train the model
- mannual: generating plot prediction vs truth mannually, consistently updating new features,keep docs up to date and update to stakeholders on time(rationale: it is important to continue to improve predictive power of the model frequently since market regime change all the time) 