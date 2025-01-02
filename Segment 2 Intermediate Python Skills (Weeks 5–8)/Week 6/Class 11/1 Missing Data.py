import pandas as pd

# Load dataset
df = pd.read_csv('sample_data.csv')

# Display original data with missing values
print("Original Data:")
print(df.info())

# Handling missing values
# 1. Dropping rows with missing values
df_dropna = df.dropna()
print("\nData after dropping rows with missing values:")
print(df_dropna.info())

median_age = df['Age'].median()

def fill_age(row):
    if pd.isna(row['Age']):
        # Find rows with the same name and a non-missing age
        same_name_rows = df[df['Name'] == row['Name']]
        valid_age = same_name_rows['Age'].dropna()
        # Return the first valid age found or the median
        if not valid_age.empty:
            return valid_age.iloc[0]
        else:
            return median_age
    return row['Age']

# 2. Filling missing values with specific values
df_fillna = df.fillna({
    'Name': 'Unknown',
    'Country': 'Unknown',
    'Salary': df['Salary'].mean()
})
df_fillna['Age'] = df_fillna.apply(fill_age, axis=1)
print("\nData after filling missing values:")
print(df_fillna.info())

# Save the cleaned data
df_fillna.to_csv('cleaned_data.csv', index=False)
print("\nCleaned data saved to 'cleaned_data.csv'")
