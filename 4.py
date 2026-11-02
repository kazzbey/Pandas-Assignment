import pandas as pd

df = pd.read_csv("sales_data_sample.csv")

# Total purchases by customer
total_purchases = df.groupby("CUSTOMERNAME")["SALES"].sum()

# Number of unique orders
orders = df.groupby("CUSTOMERNAME")["ORDERNUMBER"].nunique()

# Top five customers
top_customers = total_purchases.sort_values(
    ascending=False
).head(5)

print("Top 5 Customers:")
print(top_customers)

# Customer segmentation
customer_value = pd.qcut(
    total_purchases,
    q=3,
    labels=["Low Value", "Medium Value", "High Value"]
)

print("\nCustomer Segmentation:")
print(customer_value)

# Combine customer information
customer_report = pd.DataFrame({
    "Total Purchases": total_purchases,
    "Total Orders": orders,
    "Customer Category": customer_value
})

print("\nComplete Customer Report:")
print(customer_report)