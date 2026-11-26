# Data Quality Report

Dataset: Telecom Customer Churn

Rows: 7043
Columns: 21

Issues Identified:

- TotalCharges stored as object datatype
- 11 blank values detected in TotalCharges
- Missing values removed
- Duplicate records checked
- Data types standardized

Cleaning Actions:

- Converted TotalCharges to numeric
- Removed invalid records
- Engineered TenureGroup
- Created AvgMonthlySpend
- Encoded categorical features

Status: Cleaned dataset ready for analysis and modeling.