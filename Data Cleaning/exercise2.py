
'''
1. Display all courses with rating above 4.5
2. Create a new column called EstimatedRevenue by multiplying Price * StudentsEnrolled.
3. How many courses has Anita Sharma published? What is her average rating?
4. Show how many courses are there in each category.
5. Display names of courses that are not published.
6. Find the course with the highest number of students.
7. Show average course rating per category.
8. Export all courses with price above ₹1000 into a new CSV: premium_courses.csv
9. For each instructor, show total courses, total students, and average rating.
10. Show all published courses in Data Science, sorted by rating (highest to lowest).
11. Create a column Level:
if price > 1000 = 'Advanced'
if price between 500-1000 = 'Intermediate'
else = Beginner

'''

# Importing the necessary library
import pandas as pd

# Importing the dataset
df = pd.read_csv("courses.csv")

# Printing the dataset
print(df)

# Displaying all the courses with rating >4.5
print("\nThe courses with rating greater than 4.5 are: ")
print(df[df['Rating']>4.5])

# Creating a new column called EstimatedRevenue by multiplying Price * StudentsEnrolled.
df['EstimatedRevenue'] = df['Price'] * df['StudentsEnrolled']
print(df[['CourseName', 'EstimatedRevenue']])

print(df)      # to check whether the new column has been added to the dataframe or not

# The number of courses Anita Sharma has published, and her avg rating:
anita_df = df[df['Instructor'] == 'Anita Sharma']

print("Courses by Anita: ", len(anita_df))
print("Average rating of Anita Sharma: ", anita_df['Rating'].mean())

# Number of courses are there in each category:
print("Number of courses in each category are: \n", df['Category'].value_counts())  # value_counts is used to count the frequency of unique values in a Series or Index.

# Displaying the names of courses that are not published:
print("\nThe number of courses that aren't published are:")
print(df[df['IsPublished'] == 'No'][['CourseName', 'Instructor']])

# Course with the highest number of students:
max_enrolled = df[df['StudentsEnrolled'] == df['StudentsEnrolled'].max()]
print("\n Course with the highest number of students is:\n",max_enrolled[['CourseName', 'StudentsEnrolled']])

# Showing average course rating per category:
print("The average course rating per category is:\n",df.groupby('Category')['Rating'].mean())   # groupby()= The groupby() function in Pandas splits all the records from a data set into different categories or groups, offering flexibility to analyze the data by these groups.
# The code print(df.groupby('Category')['Rating'].mean()) uses groupby to group the data in the DataFrame df by the unique values in the 'Category' column. Once the data is grouped, the mean() function is applied to the 'Rating' column within each group to calculate the average rating for each category. 


# Exporting all courses with price above ₹1000 into a new CSV: premium_courses.csv
df[df['Price']>1000].to_csv("premium_courses.csv", index=False)
print("The courses with price more than 1000 are exported into a new csv successfully")

# For each instructor, show total courses, total students, and average rating.
print(df.groupby('Instructor').agg({
    'CourseID' : 'count',
    'StudentsEnrolled' : 'sum',
    'Rating' : 'mean'
}).rename(columns={
    'CourseID': 'TotalCourses',
    'StudentsEnrolled' : 'TotalStudents',
    'Rating' : 'AvgRating'
}))

'''
agg() -> you're telling pandas what to calculate for each group
{
    'CourseID': 'count',           # Count of courses per instructor
    'StudentsEnrolled': 'sum',     # Total students per instructor
    'Rating': 'mean'               # Average rating of their courses
}

| Method           | What It Does                                     |
| ---------------- | ------------------------------------------------ |
| `groupby('col')` | Groups the DataFrame by a column’s unique values |
| `agg({...})`     | Applies one or more aggregations per group       |
| `count`          | Counts non-null values                           |
| `sum`            | Sums up values in each group                     |
| `mean`           | Calculates average of each group                 |
| `rename()`       | Renames resulting columns                        |

'''

# Showing all published courses in Data Science, sorted by rating (highest to lowest).
result = df[(df['IsPublished'] == 'Yes') & (df['Category'] == 'Data Science')]
print('All published courses in Data Science are:\n ',result.sort_values(by = 'Rating', ascending = False))

# 11. Create a column Level:
# if price > 1000 = 'Advanced'
# if price between 500-1000 = 'Intermediate'
# else = Beginner


def get_level(price):
    if price > 1000:
        return "Advanced"
    elif price >= 500:  
        return "Intermediate"
    else:
        return "Beginner"

'''
it defined a function called get_level
it takes one argument, price
based on it, it returns the value as per the question

'''

df['Level'] = df['Price'].apply(get_level)

'''
df['Price'] is a series/column containing the price of the courses
df['Level'] is the new column we were asked to add
.apply(get_level) -> applies the get_level() to each value for each row of 'Price' column
That new series is stored in a column called "Level"

'''

print(df[['CourseName', 'Level']])


