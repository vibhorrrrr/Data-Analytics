import pandas as pd

# Sample Dataset
data = {
    'Name': ['Amit', 'Cassidy', 'Ali', 'Lopez'],
    'Age' : [25, 30, 22, 35],
    'Gender' : ['M', 'F', 'M', 'F'],
    'Income' : [50000, 60000, 52000, 58000]
}

# storing in df
df = pd.DataFrame(data)

# print df
print(df)

# Descriptive Statistics
print("Mean Age: ", df['Age'].mean())
print("Mean Income: ", df['Income'].mean())
print("Standard Deviation of Income: ", df['Income'].std())
print("Variance of Income:", df['Income'].var())
