import pandas as pd

df = pd.read_csv("data.csv")

print(df.columns)

# We remove extra spaces from column names:
df.columns = df.columns.str.strip()

print(df[df['Age'] > 22])
print(df[df['Salary'] >= 50000 ])


