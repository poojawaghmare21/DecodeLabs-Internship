import pandas as pd

# Load dataset
df = pd.read_excel("Dataset for Data Analytics.xlsx")

# TASK 1: Dataset Overview

print("========== TASK 1: DATASET OVERVIEW ==========")

print("\nNumber of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nColumn Names:")
for column in df.columns:
    print(column)

print("\nFirst 5 Rows:")
print(df.head())

# TASK 2: Basic Statistics

print("\n========== TASK 2: BASIC STATISTICS ==========")

numeric_columns = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]

for column in numeric_columns:
    print("\n-----------------------------")
    print("Column:", column)
    print("Count :", df[column].count())
    print("Mean  :", round(df[column].mean(), 2))
    print("Median:", round(df[column].median(), 2))

# TASK 3: Trend Analysis

print("\n========== TASK 3: TREND ANALYSIS ==========")

# Convert Date column into datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Create Month column
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# Monthly orders and revenue
monthly_analysis = df.groupby("Month").agg(
    Orders=("OrderID", "count"),
    Revenue=("TotalPrice", "sum")
)

print("\nMonthly Orders and Revenue:")
print(monthly_analysis.round(2))

# Highest order month
highest_orders_month = monthly_analysis["Orders"].idxmax()
highest_orders = monthly_analysis["Orders"].max()

# Highest revenue month
highest_revenue_month = monthly_analysis["Revenue"].idxmax()
highest_revenue = monthly_analysis["Revenue"].max()

print("\nHighest Number of Orders:")
print(highest_orders_month, "->", highest_orders, "orders")

print("\nHighest Revenue Month:")
print(highest_revenue_month, "->", round(highest_revenue, 2))


# Monthly Revenue Trend Graph

import matplotlib.pyplot as plt

plt.figure(figsize=(14, 6))

plt.plot(
    monthly_analysis.index,
    monthly_analysis["Revenue"],
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.xticks(rotation=90)
plt.grid()

plt.tight_layout()

plt.savefig("monthly_revenue_trend.png")

# TASK 4: Outlier Detection

print("\n========== TASK 4: OUTLIER DETECTION ==========")

# Columns for outlier analysis
outlier_columns = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]

for column in outlier_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    print("\n-----------------------------")
    print("Column:", column)
    print("Q1:", round(Q1, 2))
    print("Q3:", round(Q3, 2))
    print("IQR:", round(IQR, 2))
    print("Number of Outliers:", len(outliers))

print("\nOutlier detection completed successfully!")

# TASK 5: DATA VISUALIZATIONS

print("\n========== TASK 5: DATA VISUALIZATIONS ==========")

import matplotlib.pyplot as plt

# 1. Product-wise Sales
product_sales = df.groupby("Product")["TotalPrice"].sum()

plt.figure(figsize=(10, 6))
product_sales.plot(kind="bar")
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("product_wise_sales.png")


# 2. Payment Method Distribution
payment_counts = df["PaymentMethod"].value_counts()

plt.figure(figsize=(8, 6))
payment_counts.plot(kind="bar")
plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("payment_method_distribution.png")


# 3. Order Status Distribution
status_counts = df["OrderStatus"].value_counts()

plt.figure(figsize=(8, 6))
status_counts.plot(kind="bar")
plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("order_status_distribution.png")


# VARIABLE CORRELATION

print("\n========== VARIABLE CORRELATION ==========")

numeric_cols = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]

correlation_matrix = df[numeric_cols].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix.round(2))

# Correlation Heatmap

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))

plt.imshow(correlation_matrix, cmap="coolwarm")

plt.xticks(range(len(numeric_cols)), numeric_cols, rotation=45)
plt.yticks(range(len(numeric_cols)), numeric_cols)

plt.colorbar(label="Correlation")

plt.title("Correlation Between Numeric Variables")

plt.tight_layout()

plt.savefig("variable_correlation.png")

print("\nCorrelation analysis completed successfully!")

# VARIABLE DISTRIBUTIONS

print("\n========== VARIABLE DISTRIBUTIONS ==========")

numeric_cols = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

for idx, col in enumerate(numeric_cols):
    ax = axes[idx // 2][idx % 2]
    ax.hist(df[col], bins=25, edgecolor="white")
    ax.set_title(f"Distribution of {col}")
    ax.set_xlabel(col)
    ax.set_ylabel("Count")

plt.tight_layout()
plt.savefig("variable_distributions.png")

print("Variable distribution graph created successfully!")