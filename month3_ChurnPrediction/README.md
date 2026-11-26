# 📞 Telecom Customer Churn Data Preparation & Exploratory Data Analysis

## 📌 Project Overview

Customer churn is one of the most critical challenges faced by telecom companies. Acquiring new customers is significantly more expensive than retaining existing ones. This project focuses on preparing customer data for predictive modeling through comprehensive data cleaning, feature engineering, and exploratory data analysis (EDA).

The objective is to identify patterns associated with customer churn and generate actionable business insights that can help improve customer retention strategies.

---

## 🎯 Business Problem

Telecom companies experience revenue loss when customers discontinue their services. Understanding the characteristics and behaviors of customers who are likely to churn enables organizations to implement targeted retention campaigns and improve customer satisfaction.

This project aims to:

* Prepare raw customer data for analytics and machine learning.
* Identify factors influencing customer churn.
* Generate business-driven insights through data visualization.
* Create a clean dataset ready for predictive modeling.

---

## 📂 Dataset

**Dataset:** IBM Telco Customer Churn Dataset

**Source:** Kaggle

**Records:** 7,043 Customers

**Features:** 21 Variables

The dataset contains:

* Customer demographics
* Account information
* Service subscriptions
* Billing details
* Contract information
* Churn status

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Jupyter Notebook

---

## 📋 Project Workflow

### 1. Data Understanding

* Loaded dataset and examined structure.
* Reviewed feature descriptions and data types.
* Generated descriptive statistics.
* Identified missing and inconsistent values.

### 2. Data Cleaning

* Detected blank values in `TotalCharges`.
* Converted `TotalCharges` from object to numeric datatype.
* Removed invalid records.
* Checked for duplicate observations.
* Validated data quality.

### 3. Feature Engineering

Created additional features including:

#### TenureGroup

Customer tenure segmented into groups:

* 0–12 Months
* 13–24 Months
* 25–36 Months
* 37–48 Months
* 49–60 Months
* 61–72 Months

#### AvgMonthlySpend

Calculated average customer spending using:

Average Monthly Spend = TotalCharges / Tenure

#### Encoding

* Converted binary Yes/No features into numeric values.
* Applied one-hot encoding to categorical variables.

### 4. Exploratory Data Analysis (EDA)

Performed extensive analysis using:

* Churn Distribution Countplots
* Contract Type vs Churn Analysis
* Monthly Charges Distribution
* Correlation Heatmaps
* Customer Tenure Analysis
* Service Subscription Analysis

---

## 📊 Key Visualizations

### Customer Churn Distribution

Analyzed overall churn rates across the customer base.

### Contract Type vs Churn

Compared churn behavior across:

* Month-to-Month Contracts
* One-Year Contracts
* Two-Year Contracts

### Monthly Charges vs Churn

Evaluated the relationship between customer spending and churn.

### Correlation Heatmap

Identified relationships between numerical variables and churn indicators.

---

## 🔍 Key Insights

### Insight 1

Customers with month-to-month contracts exhibit significantly higher churn rates compared to customers with long-term contracts.

### Insight 2

Customers with higher monthly charges are more likely to churn.

### Insight 3

New customers (0–12 months tenure) demonstrate the highest churn behavior.

### Insight 4

Fiber optic internet customers show higher churn rates than DSL customers.

### Insight 5

Electronic check payment users have a greater tendency to churn.

---

## 💡 Business Recommendations

### Improve Customer Onboarding

Develop engagement programs targeting customers within their first year.

### Promote Long-Term Contracts

Offer incentives encouraging migration from month-to-month plans to annual contracts.

### Review Pricing Strategy

Evaluate pricing models for customers with high monthly charges.

### Improve Service Quality

Investigate customer satisfaction among fiber optic subscribers.

### Build Retention Programs

Create targeted retention campaigns for high-risk customer segments.

---

## 📁 Project Structure

```text
month3_ChurnPrediction/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── notebooks/
│   └── 01_customer_churn_eda.ipynb
│
├── visuals/
│
├── reports/
│
├── presentation/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## 📈 Results

Successfully transformed raw customer data into an analytics-ready dataset through:

* Data Cleaning
* Data Validation
* Feature Engineering
* Exploratory Data Analysis
* Business Insight Generation

The final cleaned dataset can be directly used for machine learning models such as:

* Logistic Regression
* Random Forest
* XGBoost
* Gradient Boosting
* Customer Churn Prediction Systems

---

## 🚀 Future Enhancements

* Customer Churn Prediction Model
* Feature Importance Analysis
* SHAP Explainability
* Interactive Power BI Dashboard
* Streamlit Deployment
* Automated Retention Recommendation System

---

## 👨‍💻 Author

Mirza Sharif Baig

Data Science | Machine Learning | Business Analytics

This project demonstrates practical skills in data preparation, exploratory data analysis, feature engineering, business intelligence, and customer analytics.
