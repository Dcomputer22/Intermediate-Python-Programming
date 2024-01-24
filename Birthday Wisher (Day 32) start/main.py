##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
a = {
    "Student":["David","Samuel", "Terry","Evan"],
    "Age": [27,24,22,32],
    "Country":["UK","Canada","China","USA"],
    "Course":["Python","Data Structures", "Machine Learning", "Web Development"],
    "Marks":[85,72,89,76]
}
df1 = pd.DataFrame(a)
print(df1)
b = df1[["Country", "Course"]]
c = df1["Student"]
print(type(c))

df2 = df1
print(df2.iloc[2:4, 'Age'])
print(df2.iloc[0:2, 0:3])
print(df2.loc[2:3, 'Country':'Course'])
