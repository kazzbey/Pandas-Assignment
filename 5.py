import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("sales_data_sample.csv", encoding="cp1252")

# Select input features
X = df[[
    "QUANTITYORDERED",
    "PRICEEACH",
    "MSRP",
    "PRODUCTLINE"
]]

# Select target
y = df["DEALSIZE"]

# Remove records with missing target
valid = y.notna()
X = X[valid]
y = y[valid]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Convert categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ("category", OneHotEncoder(handle_unknown="ignore"),
         ["PRODUCTLINE"])
    ],
    remainder="passthrough"
)

# Create Random Forest model
model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])

# Train model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

print("Predictions:")
print(y_pred)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy * 100, "%")