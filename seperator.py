import pandas as pd

# if your file uses tabs, pipes, semicolons, or other characters instead of commas, use sep

df = pd.read_csv("data.csv", sep='|')

print(df)