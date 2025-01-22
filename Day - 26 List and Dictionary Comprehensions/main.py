
""" List Comprehensions """
#
# new_item is the item that is going to be stored it can be 'item * 2' as an example.
# # new_list = [new_item for item in list]

# numbers = [1,2,3,4]
#
# new_nums = [num + 1 for num in numbers]
# print(new_nums)

doubled_numbers = [n * 2 for n in range(1,5)]
# print(doubled_numbers)


""" conditional list comprehension """

names_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names_list if len(name) <= 4]
# print(short_names)


""" challenge - 2 """
cap_names = [n.upper() for n in names_list if len(n) > 5]
# print(cap_names)
#

""" Dictionary Comprehensions """
import random

# new_dict = {new_key:new_value for (key,value) in dict.items()}
# also can add a condition :-
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}


# example :  creating a dict with names as keys and random numbers as the scores.
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)

# example : a dict of passed students from another dict
# passed_students  = {student:score for (student,score) in students_scores.items() if score > 60}
# print(passed_students)


""" Iterate over a pandas DataFrame """

student_dict = {
    "student":["Angela", "James", "Lily"],
    "score": [68,91,82]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through
# for (key,value) in student_data_frame.items():
#     print(value)

for (index,row) in student_data_frame.iterrows():
    # print(row)
    print(row.student)
    print(row.score)