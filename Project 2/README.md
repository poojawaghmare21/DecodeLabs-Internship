# 📊 Project 2 – Exploratory Data Analysis (EDA)

## 📌 Overview

This project is part of my **Data Analytics Internship at DecodeLabs**.

The main objective is to perform **Exploratory Data Analysis (EDA)** on an order and sales dataset using Python. EDA helps us understand the data by finding statistics, trends, outliers, relationships, and distributions.

### Dataset

* **Rows:** 1200
* **Columns:** 14
* **File:** Dataset for Data Analytics.xlsx

---

## 🛠️ Tools & Libraries

* Python
* Pandas
* Matplotlib
* Excel

---

# 1. Dataset Overview

First, the dataset was loaded using Pandas and its basic structure was checked.

### Code

```python
import pandas as pd

df = pd.read_excel("Dataset for Data Analytics.xlsx")

print(df.shape)
print(df.columns)
print(df.head())
```

### Output

```text
Rows: 1200
Columns: 14
```

The first few records and column names were also displayed.

---

# 2. Basic Statistics

Basic statistics help us understand the numerical data.

* **Count** → Number of values
* **Mean** → Average value
* **Median** → Middle value

### Code

```python
numeric_columns = [
    "Quantity",
    "UnitPrice",
    "ItemsInCart",
    "TotalPrice"
]

for column in numeric_columns:
    print(column)
    print("Count:", df[column].count())
    print("Mean:", round(df[column].mean(), 2))
    print("Median:", round(df[column].median(), 2))
```

### Output

| Column      | Count |    Mean | Median |
| ----------- | ----: | ------: | -----: |
| Quantity    |  1200 |    2.95 |   3.00 |
| UnitPrice   |  1200 |  356.41 | 364.21 |
| ItemsInCart |  1200 |    5.49 |   5.00 |
| TotalPrice  |  1200 | 1053.97 | 823.62 |

### Observation

The average TotalPrice is approximately **1053.97**, while the median is **823.62**.

---

# 3. Trend Analysis

Trend analysis helps us understand how values change over time.

The Date column was converted into datetime format and monthly orders and revenue were calculated.

### Code

```python
df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_analysis = df.groupby("Month").agg(
    Orders=("OrderID", "count"),
    Revenue=("TotalPrice", "sum")
)

print(monthly_analysis)
```

### Output / Observation

* Highest number of orders: **June 2024 – 53 orders**
* Highest monthly revenue: **June 2024 – approximately 68,068.54**

A line chart was created to visualize the monthly revenue trend.

**Output:** `monthly_revenue_trend.png`

---

# 4. Outlier Detection

An **outlier** is a value that is unusually high or low compared with the other values.

The **IQR (Interquartile Range)** method was used to detect outliers.

### Formula

```text
IQR = Q3 - Q1

Lower Limit = Q1 - 1.5 × IQR
Upper Limit = Q3 + 1.5 × IQR
```

### Code

```python
Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

outliers = df[
    (df["TotalPrice"] < Q1 - 1.5 * IQR) |
    (df["TotalPrice"] > Q3 + 1.5 * IQR)
]

print("Number of Outliers:", len(outliers))
```

### Output

```text
Quantity       → 0 outliers
UnitPrice      → 0 outliers
ItemsInCart    → 0 outliers
TotalPrice     → 8 outliers
```

### Observation

The `TotalPrice` column contained **8 potential outliers** according to the IQR method.

---

# 5. Data Visualization

Matplotlib was used to create visualizations and understand the data more easily.

### Product-wise Sales

```python
product_sales = df.groupby("Product")["TotalPrice"].sum()

product_sales.plot(kind="bar")
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.savefig("product_wise_sales.png")
```

Other visualizations created:

* Product-wise Sales
* Payment Method Distribution
* Order Status Distribution
* Monthly Revenue Trend

---

# 6. Variable Correlation

**Correlation** shows the relationship between numerical variables.

Correlation values generally range from **-1 to +1**.

### Code

```python
numeric_cols = [
    "Quantity",
    "UnitPrice",
    "ItemsInCart",
    "TotalPrice"
]

correlation_matrix = df[numeric_cols].corr()

print(correlation_matrix.round(2))
```

A correlation visualization was also created using Matplotlib.

**Output:** `variable_correlation.png`

---

# 7. Variable Distribution

A distribution shows how values are spread across a variable.

Histograms were created for the numerical variables.

### Code

```python
numeric_cols = [
    "Quantity",
    "UnitPrice",
    "ItemsInCart",
    "TotalPrice"
]

for col in numeric_cols:
    plt.hist(df[col], bins=25)
    plt.title(f"Distribution of {col}")
```

### Output

A combined histogram visualization was created for:

* Quantity
* UnitPrice
* ItemsInCart
* TotalPrice

**Output:** `variable_distributions.png`

---

# 📌 Key Observations

* Dataset contains **1200 records and 14 columns**.
* Average Quantity is **2.95**.
* Average UnitPrice is **356.41**.
* Average ItemsInCart is **5.49**.
* Average TotalPrice is **1053.97**.
* June 2024 recorded the highest monthly revenue.
* 8 potential outliers were identified in TotalPrice.
* Correlation between numerical variables was analyzed.
* Numerical variable distributions were visualized using histograms.

---

## 📚 Learning Outcome

Through this project, I gained practical understanding of:

* Exploratory Data Analysis
* Descriptive Statistics
* Trend Analysis
* Outlier Detection
* Correlation
* Data Distribution
* Data Visualization using Matplotlib
* Data Analysis using Pandas

---
