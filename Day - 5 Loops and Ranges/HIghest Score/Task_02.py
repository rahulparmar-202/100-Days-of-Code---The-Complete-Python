student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# # sum of all scores using sum function
# print(sum(student_scores))

# # getting the sum of all scores by a for loop
# sum = 0
# for score in student_scores:
#     sum += score
#
# print(sum)

# getting maximum number with max function
print(max(student_scores))

# Pause - 1 : get the maximum score by using for loop
current_max = 0
print(current_max)
for score in student_scores:
    if score > current_max:
        current_max = score

print(current_max)