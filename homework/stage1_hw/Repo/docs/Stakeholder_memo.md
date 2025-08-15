
# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Excess return is a valuable trading signal for portfolio constructions and stock selection in quantitative stock investing. Predicting stocks’ future excess return allows portfolio managers to make informed decisions ahead of time, and improve portfolio strategies. This project aims to leverage reliable historical stock data (OHLCV) and benchmarks in the past 5 years from public open API like yfinance and Alpha vantage, and construct factors like momentum factors and value factors. We will use machine learning regression models as the tool predicts one day ahead excess return. Model performance will be evaluated through backtesting, and deliver actionable insights to help portfolio managers to construct strategies with stable return. 
 

## Stakeholder & User
- **Stakeholders**: portfolio managers used predictive next day excess return to make allocation decisions. Risk management managers evaluate and monitor potential risk, and ensure the trading strategies stay within the predefined risk limits.
- **Users**: Quantitative researchers update the historical data, select relevant factors, develop the predictive model for future excess return, and conduct the backtests to validate portfolio strategies. Traders execute trades based on the predictive excess return model. 

## Useful Answer & Decision
- **Predictive**: The purpose of this project is to predict next day excess return for selected stocks based on their historical data and relevant factors.
- **Metrics**: Next day excess returns are important metrics to construct portfolio strategies. Metrics like annualized return, sharpe ratio, and maximum drawdown are useful to validate strategies when conducting backtests.

## Assumptions & Constraints
- **Assumptions**: Historical data and benchmarks from public API are accurate and reliable. Assuming the relationship between factors (momentum,values) and excess return are linear.
- **Constraints**: Daily historical data are limited to the past 5 years. No transaction cost, slippage, or liquidity constraints are considered in the initial version. Models are limited to predict next day excess return only.

## Known Unknowns / Risks
**Uncertain risks:** 
- Missing data in particular trade days
- Model overfitting may lead to bad performace in backtests

## Lifecycle Mapping
Goal → Stage → Deliverable
- `\<Goal A\>` → Problem Framing & Scoping (Stage 01) → `\<Deliverable X\>`

## Repo Plan
/data/, /src/, /notebooks/, /docs/ ; cadence for updates

