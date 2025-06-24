import pandas as pd

df = pd.DataFrame(data = {
    'Name' : ['Amit', 'Ajay', 'Alisha', 'Ram', 'Bunny'],
    'Age'  : ['21', '42', '22', 'EKVEES', '11'],
    'Salary': [20000, 50000, 24000, 23000, 21000],
    'Department':['IT', 'HR', 'Management', 'IT', 'HR']
})

print(df)

# Output: 
''' 
     Name Age  Salary  Department
0    Amit  21   20000          IT
1    Ajay  42   50000          HR
2  Alisha  22   24000  Management
3     Ram  21   23000          IT
4   Bunny  11   21000          HR
'''

# Check the current datatypes of the columns
print(df.dtypes)

# Output
'''
Name          object
Age           object    <- Should be int/float
Salary         int64
Department    object
dtype: object
'''

# Convert String to Numeric
df['Age'] = pd.to_numeric(df['Age'], errors = 'coerce')

# You can use errors='coerce' to turn non-numeric values into NaN.
df['Age'] = pd.to_numeric(df['Age'], errors = 'coerce')
'''
The line df['Age'] = pd.to_numeric(df['Age'], errors = 'coerce') 
converts the 'Age' column of the DataFrame df to a numeric type. 
If there are any non-numeric values in the 'Age' column, they will 
be replaced with NaN (Not a Number) instead of raising an error.
This is useful for handling data that may contain invalid or non-numeric 
entries, allowing the conversion to proceed without interruption.
The errors='coerce' parameter ensures that any parsing errors result 
in NaN values, which can then be handled separately if needed.
'''

print(df.dtypes)
print(df)


# Convert to date:
# df['JoiningDate'] = pd.to_datetime(df['JoiningDate'])


