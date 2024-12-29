
# Range function : with for loop

# range(a, b, step) : but does not include b ,[ it does from 'a' to 'b-1' ]
#  step is basically the jump between the numbers you want. like step = 2 will be 0,2,4,6,8,10

# for i in range(0,11, 2):
#     print(i)

# PAUSE 1 - The Gauss Challenge
#  count 1 to 100 by using range() with for loop

count = 0
for num in range(1, 101):
    count += num
print(count)