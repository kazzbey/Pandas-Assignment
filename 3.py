import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="cp1252")

# Convert date into datetime format
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])

# Extract year and month
df["YEAR"] = df["ORDERDATE"].dt.year
df["MONTH"] = df["ORDERDATE"].dt.month

# Monthly sales
monthly_sales = df.groupby(["YEAR", "MONTH"])["SALES"].sum()

print("Monthly Sales:")
print(monthly_sales)

# Yearly sales
yearly_sales = df.groupby("YEAR")["SALES"].sum()

print("\nYearly Sales:")
print(yearly_sales)

# Highest revenue month
print("\nHighest Revenue Month:", monthly_sales.idxmax())
print("Highest Revenue:", monthly_sales.max())