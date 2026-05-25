# Developers Hub Corporation (DHC) - Advanced Data Science Internship Portfolio

## Portfolio Overview
This repository contains my final submissions for the **Advanced Data Science & Analytics Internship** at Developers Hub Corporation (DHC). It showcases 5 comprehensive, end-to-end data pipelines covering supervised machine learning, unsupervised clustering, chronological forecasting, economic cost optimization, and operational business intelligence dashboards.

---

## 🛠️ Complete Task Index & Implementation Breakdown

### 📂 [Task 1: Term Deposit Subscription Prediction](./Task1_Term_Deposit_Prediction/)
* **Objective:** Optimize banking telemarketing conversion by predicting customer term deposit subscriptions (`deposit = yes`).
* **Methodology:** Scaled features via `StandardScaler`, handled data splits with stratification, and evaluated a Logistic Regression baseline against an optimized Random Forest Ensemble (~91% Accuracy, 0.958 AUC).
* **Explainable AI (XAI):** Integrated `SHAP` (Beeswarm and Summary charts) for global variable dynamics and `LIME` Tabular Explainer models to interpret 5 individual customer profiles.

### 📂 [Task 2: Customer Segmentation via Unsupervised Learning](./Task2_Customer_Segmentation/)
* **Objective:** Segment consumer demographic segments to transition from uniform marketing to personalized, data-driven outreach strategies.
* **Methodology:** Handled geometric distribution modeling via K-Means clustering. Optimized the target cluster scale ($K=5$) using WCSS Elbow plots and Silhouette Scores.
* **Dimensional Reduction:** Applied **PCA (Linear)** alongside **t-SNE (Non-Linear)** manifolds to project customer clusters into clear 2D visual maps.

### 📂 [Task 3: Household Energy Time Series Forecasting](./Task3_Energy_Forecasting/)
* **Objective:** Forecast short-term active power usage patterns to improve utility grid load balancing.
* **Methodology:** Resampled minutely tracking logs into Daily Means to capture macro seasonality. Engineered timestamp features (Month, Day of week, Weekend flags) alongside lookback lag parameters (`Lag_1_Day`, `Lag_7_Days`).
* **Contenders Evaluated:** Built and compared Classical **ARIMA (1,1,1)**, **Facebook Prophet**, and an **XGBoost Regressor** across a 30-day testing window using MAE and RMSE performance scores.

### 📂 [Task 4: Credit Default Risk with Cost Optimization](./Task4_Credit_Risk_Optimization/)
* **Objective:** Build a credit scoring model that minimizes a bank's total financial exposure rather than just optimizing abstract machine learning metrics.
* **Methodology:** Cleansed applicant profiles and implemented an advanced `CatBoost Classifier`.
* **Financial Optimization Layer:** Built an economic loss matrix mapping real-world asymmetric banking penalties: False Positives (lost profit on a false rejection = \$500) vs False Negatives (loan write-offs = \$5,000). Programmatically shifted the decision threshold away from the default 0.50 cutoff to minimize total institutional portfolio loss.

### 📂 [Task 5: Interactive BI Dashboard in Streamlit](./Task5_BI_Streamlit_Dashboard/)
* **Objective:** Build a data-driven web app for real-time sales and portfolio analysis using the Global Superstore Dataset.
* **Methodology:** Created an interactive **Streamlit Web Application** driven by Plotly Express charts.
* **Features:** Implemented hierarchical category filtering, live calculated KPI scorecards tracking Revenue, Net Profit, and Profit Margins, alongside horizontal leaderboards mapping the Top 5 customer accounts.

---

## 🏁 Final Portfolio Performance Overview Matrix

| Milestone Assignment | Core Architecture Engine | Primary Performance Metric | Key Business Discovery / Outcome |
| :--- | :--- | :--- | :--- |
| **Task 1: Marketing Prediction** | Random Forest + SHAP/LIME | **0.958 ROC-AUC** | Call duration & prior campaign success dictate client conversion. |
| **Task 2: Customer Segments** | K-Means + PCA + t-SNE | **Optimal Silhouette Score** | Isolated 5 distinct customer personas for targeted marketing. |
| **Task 3: Energy Forecasting** | Facebook Prophet + XGBoost | **Lowest MAE / RMSE** | Weekend usage cycles and 7-day lookbacks drive consumption predictability. |
| **Task 4: Credit Risk Scoring** | CatBoost + Custom Cost Function | **Minimized Financial Loss** | Lowering risk cutoffs protects bank capital from expensive write-offs. |
| **Task 5: Business Dashboard** | Streamlit + Plotly Engine | **Live Reactive KPIs** | Enabled instantaneous regional revenue and profit margin analytics. |

---

## 🚀 Step-by-Step Instructions to Run This Project Locally
1. Clone this entire portfolio repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
