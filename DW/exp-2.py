import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
# Step 1: Create a sample dataset
data = {
 'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Alice'],
 'Age': [25, 30, np.nan, 45, 28, 25],
 'Salary': [50000, 60000, 55000, np.nan, 52000, 50000],
 'Department': ['HR', 'IT', 'IT', 'Finance', np.nan, 'HR']
}
df = pd.DataFrame(data)
print("Original Dataset:")
print(df)
# Step 2: Drop duplicate rows
df = df.drop_duplicates()
# Step 3: Handle missing values
# Fill numeric columns with mean
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
# Fill categorical columns with mode
categorical_cols = df.select_dtypes(include=['object']).columns
df[categorical_cols] =
df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])
# Step 4: Normalize numeric columns using Min-Max scaling
scaler = MinMaxScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
print("\nCleaned and Normalized Dataset:")
print(df)
