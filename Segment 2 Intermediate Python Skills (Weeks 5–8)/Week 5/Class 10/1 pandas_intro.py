import pandas as pd

# Creating a Series
series = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("Series:\n", series)

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Accessing Columns and Rows
print("Column (Name):\n", df['Name'])
print("Row 1 (iloc):\n", df.iloc[1])
print("Row with Name Bob (loc):\n", df.loc[df['Name'] == 'Bob'])
