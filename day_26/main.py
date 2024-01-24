import random
import pandas
# List Comprehension
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Fatima"
new_list = [letter for letter in name]
print(new_list)

# Using the format new_list = [new_item for item in list]
double_numbers = [i * 2 for i in range(1,5)]
print(double_numbers)

# Conditional List Comprehension
names = ["Fatima", "Zainab", "Samad", "James", "Jude", "Sam", "Tobi"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) >= 5]
print(short_names)
print(long_names)

# Dictionary Comprehension
# To loop through list
## new_dict = {new_key: new_value for values in list}
students = ["Promise", "Samuel", "Tobi", "Tofunmi", "Victoria", "Yemisi"]
students_scores = {student:random.randint(1, 100) for student in students}
print(students_scores)

# To loop through dictionaries
## new_dict = {new_key: new_value for (key, value) in dict.items()}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)
# For Conditional Dictionary Comprehension
## new_dict = {new_key: new_value for (key, value) in dict.items() if test}

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)

# Looping through Dataframe
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# for (key,value) in student_data_frame.items():
#     print(key)
# Data frame has a function that can loop through each row it's called iterrows
for (index, row) in student_data_frame.iterrows():
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "Lily":
        print(row.score)
