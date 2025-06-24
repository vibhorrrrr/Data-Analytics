import pandas as pd

df = pd.read_csv("data.csv")

print(df)

print(df.head())    # First 5 rows

print(df.tail(2))   # Last 2 rows

print(df.shape)     # (rows, columns)

print(df.columns)   # column names

print(df.dtypes)    # Data types of columns

print(df.info())    # Summary

print(df.describe())