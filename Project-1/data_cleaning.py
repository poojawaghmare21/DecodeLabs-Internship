import pandas as pd
print(pd.__version__)

file = pd.ExcelFile("Data Analytics Project 1.xlsx")

print(file.sheet_names)

df = pd.read_excel("Data Analytics Project 1.xlsx", sheet_name="Sheet1")

print(df.head())
print(df.shape)

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

df["CouponCode"] = df["CouponCode"].fillna(0)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate OrderIDs:")
print(df["OrderID"].duplicated().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

df["Date"] = pd.to_datetime(df["Date"], errors="coerce").dt.date

print("\nInvalid Dates:")
print(df["Date"].isna().sum())

print("\nNumeric Column Data Types:")
print(df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].dtypes)

df.to_excel("Cleaned_Data_Python.xlsx", index=False)
print("\nCleaned data saved successfully!")
