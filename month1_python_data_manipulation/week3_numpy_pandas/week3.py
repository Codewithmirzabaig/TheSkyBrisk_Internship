# ==========================================
# WEEK 3 – NUMPY AND PANDAS DATA MANIPULATION
# ==========================================

import os
import numpy as np
import pandas as pd


# ---- NumPy Operations ----
def numpy_operations():
    numbers = np.array([10, 20, 30, 40, 50])

    print("\nNumPy Array:", numbers)
    print("Mean:", np.mean(numbers))
    print("Maximum:", np.max(numbers))
    print("Minimum:", np.min(numbers))
    print("Standard Deviation:", np.std(numbers))


# ---- Load Dataset ----
def load_dataset():
    file_path = os.path.join(os.path.dirname(__file__), "sample_sales_data.csv")

    df = pd.read_csv(file_path)

    print("\nOriginal Dataset:")
    print(df)

    return df


# ---- Clean Dataset ----
def clean_dataset(df):
    print("\nMissing Values Before Cleaning:")
    print(df.isnull().sum())

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing Quantity with average quantity
    df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())

    # Fill missing Price with average price
    df["Price"] = df["Price"].fillna(df["Price"].mean())

    print("\nMissing Values After Cleaning:")
    print(df.isnull().sum())

    return df


# ---- Analyze Dataset ----
def analyze_dataset(df):
    df["TotalSales"] = df["Quantity"] * df["Price"]

    print("\nCleaned Dataset with Total Sales:")
    print(df)

    print("\nAverage Sales by Category:")
    print(df.groupby("Category")["TotalSales"].mean())

    print("\nTotal Sales by City:")
    print(df.groupby("City")["TotalSales"].sum())

    print("\nTotal Quantity Sold by Product:")
    print(df.groupby("Product")["Quantity"].sum())


# ---- Main Function ----
def main():
    print("\n--- WEEK 3 PROGRAM: NUMPY AND PANDAS ---")

    numpy_operations()

    df = load_dataset()
    cleaned_df = clean_dataset(df)
    analyze_dataset(cleaned_df)


if __name__ == "__main__":
    main()