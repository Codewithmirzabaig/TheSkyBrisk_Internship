# ==========================================
# WEEK 4 – DATA VISUALIZATION
# ==========================================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ---- Load Dataset ----
def load_dataset():
    file_path = os.path.join(os.path.dirname(__file__), "sample_sales_data.csv")
    df = pd.read_csv(file_path)
    return df


# ---- Clean Dataset ----
def clean_dataset(df):
    df = df.drop_duplicates()

    df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())
    df["Price"] = df["Price"].fillna(df["Price"].mean())

    df["TotalSales"] = df["Quantity"] * df["Price"]

    return df


# ---- Create Plots Folder ----
def create_plots_folder():
    plots_path = os.path.join(os.path.dirname(__file__), "plots")

    if not os.path.exists(plots_path):
        os.makedirs(plots_path)

    return plots_path


# ---- Histogram ----
def create_histogram(df, plots_path):
    plt.figure(figsize=(8, 5))
    plt.hist(df["TotalSales"])
    plt.title("Distribution of Total Sales")
    plt.xlabel("Total Sales")
    plt.ylabel("Frequency")
    plt.savefig(os.path.join(plots_path, "histogram_total_sales.png"))
    plt.close()


# ---- Scatter Plot ----
def create_scatter_plot(df, plots_path):
    plt.figure(figsize=(8, 5))
    plt.scatter(df["Quantity"], df["TotalSales"])
    plt.title("Quantity vs Total Sales")
    plt.xlabel("Quantity")
    plt.ylabel("Total Sales")
    plt.savefig(os.path.join(plots_path, "scatter_quantity_sales.png"))
    plt.close()


# ---- Bar Chart ----
def create_bar_chart(df, plots_path):
    category_sales = df.groupby("Category")["TotalSales"].sum()

    plt.figure(figsize=(8, 5))
    category_sales.plot(kind="bar")
    plt.title("Total Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.savefig(os.path.join(plots_path, "bar_total_sales_category.png"))
    plt.close()


# ---- Heatmap ----
def create_heatmap(df, plots_path):
    numeric_df = df[["Quantity", "Price", "TotalSales"]]

    plt.figure(figsize=(8, 5))
    sns.heatmap(numeric_df.corr(), annot=True)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(os.path.join(plots_path, "heatmap_correlation.png"))
    plt.close()


# ---- Main Function ----
def main():
    print("\n--- WEEK 4 PROGRAM: DATA VISUALIZATION ---")

    df = load_dataset()
    df = clean_dataset(df)
    plots_path = create_plots_folder()

    create_histogram(df, plots_path)
    create_scatter_plot(df, plots_path)
    create_bar_chart(df, plots_path)
    create_heatmap(df, plots_path)

    print("Visualizations created successfully.")
    print("Check the plots folder.")


if __name__ == "__main__":
    main()