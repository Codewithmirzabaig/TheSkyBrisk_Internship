# Executive Summary

## Project Overview

This project analyzes customer churn behavior in a telecom company using the IBM Telco Customer Churn dataset. The objective was to prepare customer data for future predictive modeling through data cleaning, feature engineering, and exploratory data analysis (EDA).

## Dataset Summary

* Total Records: 7,043 customers
* Features: 21 customer attributes
* Target Variable: Churn
* Data Source: IBM Telco Customer Churn Dataset (Kaggle)

## Data Preparation

Several data quality issues were identified and resolved:

* Converted TotalCharges from object to numeric datatype
* Removed invalid and missing records
* Validated data consistency
* Created new analytical features such as TenureGroup and AvgMonthlySpend
* Encoded categorical variables for analysis

## Key Findings

### 1. Contract Type Strongly Influences Churn

Customers on month-to-month contracts exhibit significantly higher churn rates compared to customers with long-term contracts.

### 2. New Customers Are at Highest Risk

Customers with shorter tenure periods are more likely to leave the service.

### 3. Higher Monthly Charges Increase Churn Probability

Customers paying higher monthly fees demonstrate a greater tendency to churn.

### 4. Fiber Optic Customers Show Elevated Churn

Fiber optic subscribers experience higher churn rates than DSL customers.

### 5. Electronic Check Users Have Higher Churn

Customers using electronic check payment methods are more likely to discontinue services.

## Business Recommendations

* Encourage migration to long-term contracts through promotional offers.
* Implement onboarding and engagement programs for new customers.
* Review pricing strategies for high-cost plans.
* Investigate customer satisfaction among fiber optic users.
* Develop targeted retention campaigns for high-risk customer segments.

## Conclusion

The analysis successfully transformed raw customer data into an analytics-ready dataset and identified several key drivers of customer churn. These insights can support customer retention initiatives and serve as a foundation for future machine learning models aimed at predicting churn and improving business performance.
