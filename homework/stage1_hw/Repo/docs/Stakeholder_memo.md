
# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
We aim to determine whether the trading strategy is valid for deploy in the real world market.In order to validate the trading strategy, it is important to run backtest with historical data from the stock market, and judge the validation
of the trading strategy by important metrics like annualized return, maximum drawdown, and sharpe ratio. It matters for portfolio managers to deploy
the stratgey or not. 

## Stakeholder & User
Decision makes are usually portfolio managers. The users are usually quant reasearch team, risk management team, and traders. In order to complete
the task, we need to develop the backtest framework in the beginning, and collect high frequency historical price data(OHLCV). Then we use the trading 
strategy we want to validate to run the backtest, and check important metrics.

## Useful Answer & Decision
We are looking for descriptive answers from the backtest about the performance of the trading stratgey with historical data. Metrics like
sharpe ratio, maximum drawdown, annualized return are important to judge the performance of the stratgey, and deliver to the decison makers
simultaneously.

## Assumptions & Constraints
data availability: using public API to collect reliable data such as yfinance and alpha vantage<br>
Compliance: never use future data to run the backtest

## Known Unknowns / Risks
uncertain risks: missing data, include holidays as trade days, wrong adjustment

## Lifecycle Mapping
Goal → Stage → Deliverable
- `\<Goal A\>` → Problem Framing & Scoping (Stage 01) → `\<Deliverable X\>`

## Repo Plan
/data/, /src/, /notebooks/, /docs/ ; cadence for updates

