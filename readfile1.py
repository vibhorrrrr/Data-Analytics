import pandas as pd

# usecols is used to read the selected columns

df = pd.read_csv("data.csv", usecols=['Name', 'Salary'])

print(df)