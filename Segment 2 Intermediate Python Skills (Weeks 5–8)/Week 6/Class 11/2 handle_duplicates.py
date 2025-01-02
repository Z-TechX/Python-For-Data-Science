
import pandas as pd

# Load dataset
df = pd.read_csv('cleaned_data.csv')

# Display original data
print("Cleaned Data:")
print(df)

# Identifying duplicates
# Trim spaces and convert all data to uppercase
trim = df.applymap(lambda x: x.strip().upper() if isinstance(x, str) else x)
duplicates = df[trim.duplicated()]
print("\nDuplicate rows:")
print(duplicates)

# Removing duplicates
df_no_duplicates = df.drop_duplicates()
print("\nData after removing duplicates:")
print(df_no_duplicates)

# Save the deduplicated data
df_no_duplicates.to_csv('deduplicated_data.csv', index=False)
print("\nDeduplicated data saved to 'deduplicated_data.csv'")
