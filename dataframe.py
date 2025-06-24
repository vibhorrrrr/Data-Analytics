import pandas as pd

data = {
    'Name':['Amit', 'Ram', 'Lopez', 'Shyam'],
    'Age' : [22, 21, 25, 27],
    'Salary' : [50000, 60000, 25000, 65000]
}

df = pd.DataFrame(data)

print(df)