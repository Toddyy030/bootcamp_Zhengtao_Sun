## Deployment & Monitoring reflection

## 1. risk if deployed
There are several risks which should be noticed before the deployment. First, the market regime change all the time, the features I choose might not fit linear relationship with the target I tried to predict. Second, cleaning strategy like removing outliers might discard important financial events, and reduce the predictive power of the model. Also, the features I choose like momentum, volatility, and log daily return can be influenced by the noise. 
## 2. Monitoring metrics across layers (Data/Model/System/Business)
- data: freshness minutes, %nulls by columns, schema hash
- Model: track 20 days rolling MAE/AUC, calibration, stability index
- System: p95 latency(<250ms), error rate(<1%), availability(>99%)
- Business: approval rate, bad rate, revenue per decision
## 3. ownership & handoffs:
Data Science and Machine Learning teams own selecting features, retraining model, and review model quality; Platform is on-call for system; the financial Analyst runs the model weekly review to consider the predictive power of the model. Rollback is approved by the Data Scientist and machine learning group and executed by Platform; Data Science team also need to update the dashboard and change log.