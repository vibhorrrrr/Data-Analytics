import pandas as pd

df = pd.read_csv("data.csv")


# Accessing Columns: 
print(df['Name'])               # Single Column

print(df[['Name', 'Salary']])   # Multiple Column

# Accessing Rows by positions:
print(df.iloc[0])               # First Row

print(df.iloc[1:3])             # Slice of Rows- df.iloc[1:3] selects rows with indices 1 and 2 (since the end index in a slice is exclusive). This means the output will include the second and third rows of the DataFrame.


# Accessing Rows by Conditions:
print(df[['Name', 'Salary', 'Age']])   # Multiple Columns
print(df[df['Age'] > 22])

