import pandas as pd

# Importing a Dataset
df = pd.read_csv('example.csv')  # Replace 'example.csv' with a real dataset file path

# Basic Exploration
print("Head of Dataset:\n", df.head())
print("Summary Statistics:\n", df.describe())
print("Column Names:", df.columns)
print("Shape of DataFrame:", df.shape)
print("Null Values:\n", df.isnull().sum())

# Filtering Data
filtered = df[df['Age'] > 30]
print("Filtered Rows (Age > 30):\n", filtered)
