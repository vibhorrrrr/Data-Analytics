'''
Load the CSV into a DataFrame

- Show the first 3 rows

- Display names of employees with salary > 58000

- Count number of rows in the dataset

- Export all HR employees to a new CSV file

'''

# Solution:

# importing the necessary libraries:
import pandas as pd

# Loading the csv into a dataframe:
df = pd.read_csv("exercise.csv")

# We remove extra spaces from column names:
df.columns = df.columns.str.strip()

# Print dataFrame:
print("\nThe dataset is:")
print(df)

# Showing the first 3 rows:
print("\nThe First 3 rows are: ")
print(df.head(3))

# Display names of employees with Salary > 58000:
print("\nThe names of employees with salary more than 58k are:")
print(df[df['Salary']>58000])

# Count number of rows in the dataset:
print("\nThe number of rows in the dataset are: ", len(df))

# Export all HR employees to a new csv file:
df[df['Department'] == 'HR'].to_csv("hr_employees.csv", index=False)






