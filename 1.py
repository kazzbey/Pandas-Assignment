import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="cp1252")

# pd is an alias for Pandas.
# read_csv() reads your CSV file.
# df stores the dataset as a DataFrame.
# datatype of df is a dataframe


# Display first five records
print(df.head())

# Total rows and columns
print("Shape:", df.shape)
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Missing values
print(df.isnull().sum())

# Replace missing values
df["STATE"] = df["STATE"].fillna("Unknown")
df["TERRITORY"] = df["TERRITORY"].fillna("Unknown")

# Sales statistics
print("Average:", df["SALES"].mean())
print("Maximum:", df["SALES"].max())
print("Minimum:", df["SALES"].min())