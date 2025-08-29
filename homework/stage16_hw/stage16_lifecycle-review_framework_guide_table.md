# Applied Financial Engineering — Framework Guide Template

This Framework Guide is a structured reflection tool.  
Fill it in as you progress through the course or at the end of your project.  
It will help you connect each stage of the **Applied Financial Engineering Lifecycle** to your own project, and create a portfolio-ready artifact.

---

## How to Use
- Each row corresponds to one stage in the lifecycle.  
- Use the prompts to guide your answers.  
- Be concise but specific — 2–4 sentences per cell is often enough.  
- This is **not a test prep sheet**. It’s a way to *document, reflect, and demonstrate* your process.

---

## Framework Guide Table

| Lifecycle Stage | What You Did | Challenges | Solutions / Decisions | Future Improvements |
|-----------------|--------------|------------|-----------------------|---------------------|
| **1. Problem Framing & Scoping** | My project are dedicated to predict next_day excess return by applying time series and basic linear regression model and using selecting features  | Target choices were ambiguity. Tried to choose targets between predicting closing price or excess return  | I consider excess return were more important metrics in the financial market rather than close price. I'm more intereted in investigating the relationship between factors and excess return| No, I consider my problem scoping is specific enough.|
| **2. Tooling Setup** | I install multiple libraries like pandas, numpy, scikit-learn, and matplotlib to help me doing the analysis|  I was struggling to generate the requirement.txt at the particular folder| I create .env file and store the requried environment information in that file | automatically retrieve data from the API |
| **3. Python Fundamentals** | Apply numpy to do calculation, using pandas function like groupby, rolling | Yes, there is difference running time between using python for loop and numpy array | I do both code reviews and apply simple practice on grouby and np.array| I want to continue working on my skill of using numpy to do vectorization calculation, practice using grouby,rolling,and np.where|
| **4. Data Acquisition / Ingestion** | My stock data comes from public API yfinance and alpha vantage| No, There is no any access and cleanlines issues| I construct a reuseable ticker fetch function in the utils.py, and applying for loop and append to collect the stock data on my list| I want to build up a pipeline to automatically collect latest stock data(OHLCV) daily|
| **5. Data Storage** | I store my raw data from public API in the data/raw folder| Need to store large files in to parquet files | store raw data and processed data in the separate folders | I do not see any improvments I could make on data storage|
| **6. Data Preprocessing** | I drop the missing values and remove the outlier by appying IQR, winsorize, and z-score|winsorize method hurt the distribution of the original data the most| I decide on applying the IQR method to remove the outliers, and drop the missing values|  Need to compare more carefully how IQR and z-score influence the original data|
| **7. Outlier Analysis** | I use boxplot to see the outliers and apply IQR method to remove them| It is difficult to determine whether the outliers carry important information or not| I remove the ouliers if it is out of range of [Q1-1.5IQR, Q3+1.5IQR]| I will compare the effect on the original data by using different cleaning strategy|
| **8. Exploratory Data Analysis (EDA)** | I demonstrate the distribution of the daily return and close price on the stock I choose| the price up-trend looked safe; the return histogram looked almost normal but had fat tails| compare the relationship between two features using scatterplot, and demonstrate correlation matrix| splitting by year and high/low volatility|
| **9. Feature Engineering** |  momentum fatcors, volatility, rolling average, log daily return | log daily return | correlation matrix| overnight returns|
| **10. Modeling (Regression / Time Series / Classification)** | I tried linear regression and time series models| overfitting affect the predictive power of the model | I choose time series as my final model | I would try XGBoost and random forest |
| **11. Evaluation & Risk Communication** | I evaluate return and volatility| label misalignment,leakage if features aren’t shifted| I show a prediction-vs-truth chart | To be more robust: time-blocked CV, bootstrap CIs, backtests with fees/slippage, subgroup checks (by volatility/earnings days) |
| **12. Results Reporting, Delivery Design & Stakeholder Communication** | a simple README.md | why we must shift(1) to avoid leakage, and how drift/regime changes break old patterns | start with the one-page takeaway, use large clear charts| I will construct the README file with more details |
| **13. Productization** | saved model.pkl + features,exposed a tiny Flask API (POST /predict, /plot) | some feature code duplicated between notebook | fixed features order and used DataFrame with column names, shift(1) to avoid leakage | add a small runbook for rollback, schema validation,simple API key auth |
| **14. Deployment & Monitoring** | loading model.pkl | checking data freshness | track 20 days rolling MAE/AUC, calibration, stability index | using app.py and streamlit |
| **15. Orchestration & System Design** | ingest --> clean --> train --> report | generating plot prediction vs truth mannually, consistently updating new features,keep docs up to date and update to stakeholders | Solved by making steps idempotent, writing checkpoints | No, nothing I want to change |
| **16. Lifecycle Review & Reflection** |  avoiding data leakage by using (shift(1))| handling outliers/regime shifts, writing the README.md file | idempotent steps with checkpoints, fixed seeds and pinned versions | apply more advacned machine learning model|

---

## Reflection Prompts

- Which stage was the most **difficult** for you, and why? lifecycle review stage, can't answer every question in details
- Which stage was the most **rewarding**?  feature engineering
- How do the stages **connect** — where did one stage’s decisions constrain or enable later stages?  feature engineering stage connect to future modeling stages
- If you repeated this project, what would you **do differently across the lifecycle**?  I will try to apply more advanced machine learning model, and write README.md more properly
- Which skills do you most want to **strengthen** before your next financial engineering project?  I want to strength the proficiency of using pandas, numpy, and scikit learn. learning properly document my code, reflect the assumptions and risks precisely.

---