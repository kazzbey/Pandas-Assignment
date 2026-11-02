import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="cp1252")

# Total sales by product category
total_sales = df.groupby("PRODUCTLINE")["SALES"].sum()

# Average sales by product category
average_sales = df.groupby("PRODUCTLINE")["SALES"].mean()

# Sort by total sales
result = total_sales.sort_values(ascending=False)
# result,total sales and average sales all are pandas series, so we can use idxmax() to get the index of the maximum value.
print("Total Sales:")
print(result)

print("\nAverage Sales:")
print(average_sales)

# Best-performing category
print("\nBest Category:", result.idxmax())
print("Highest Revenue:", result.max())