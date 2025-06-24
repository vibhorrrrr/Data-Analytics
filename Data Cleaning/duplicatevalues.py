# Handling duplicate values

import pandas as pd

df = pd.DataFrame(data = {
    'Name':['Amit', 'Alisha', 'Alisha', 'Charlie'],
    'Age' :[25, 30, 30, 22]
})

# Detect duplicates
df.duplicated()
print(df.duplicated())

'''
0    False
1    False
2     True   <- duplicate
3    False

'''
 
# Prints duplicate rows
print(df[df.duplicated()])


# Remove duplicates:
print("\n", df.drop_duplicates())
# By default it will keep the first occurence and remove the rest

# You can also drop based on specific columns
removecol= df.drop_duplicates(subset=['Name'])

print(removecol)