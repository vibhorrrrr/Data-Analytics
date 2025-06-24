# Creating a messy DataFrame

import pandas as pd

data = {
    'Name':['Alice', 'Amit', 'Ram', 'David', None],
    'Age' :[25, None, 22, 28, 30],
    'Salary' :[50000, 60000, None, 70000, 65000],
    'Department' :['HR', 'IT', 'HR', 'Finance', None]
}

df = pd.DataFrame(data)
print(df)

# How to detect Missing values?
print(df.isnull())          # returns missing values as 'False'
print(df.isnull().sum())    # Gives the count of missing values per column:

# How to drop missing data?
# Drop all the rows that have missing values
dropped = df.dropna()
print(dropped)

# Drop rows only if all columns are missing:

'''
this will only be useful when all the column data is missing
'''

dropped_if = df.dropna(how = 'all')
print(dropped_if)

# Drop columns instead of rows
drop_column = df.dropna(axis=1)
print(drop_column)

# Fill Missing values
# Fill missing age with 0
print(df['Age'].fillna(0))

# Fill missing salary with avg salary
print(df['Salary'].fillna(df['Salary'].mean()))

# Forward fill: Use previous row's value
print(df.fillna(method='ffill'))

'''
Use Case            Example
Time Series         Fill today's temp with yesterday's
Sequential Data     Fill customer name with previous name if same ID

'''

# Backward Fill
print(df.fillna(method='bfill'))

# use inplace = True if you want to change the ORIGINAL DataFrame
# meaning: print(df.fillna(method='bfill', inplace=True)) will affect our OG DataFrame

