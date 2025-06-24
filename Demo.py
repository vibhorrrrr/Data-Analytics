
import pandas as pd

# Create simple dataset
data = {
    'Name': ['Amit', 'Ram', 'Shyam', 'Paras'],
    'Age' : [22, 21, 25, 26],
    'Income' : [30000, 40000, 35000, 37000]
}

df = pd.DataFrame(data)

# Print Data
print(df)

# Basic Statistical Operations
print("Mean Age: ", df['Age'].mean())
print("Median Income: ", df['Income'].median())
print("Mode of Income: ", df['Income'].mode()[0])

#df['Income'].mode() → Series with all modes 
#df['Income'].mode()[0] → First mode value only

print("Standard Deviation: ", df['Income'].std())
