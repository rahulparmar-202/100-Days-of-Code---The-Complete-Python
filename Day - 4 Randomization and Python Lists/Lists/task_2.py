
# lists :- they can store multiple values and with multiple data types.
# index from 0 to the (lenght of list - 1)
fruits = ["Cherry", "Apple", "Banana", "Grapes"]
print(fruits)
print(fruits[2])
print(fruits[-1])

# adding items to the list ( one at a time )
fruits.append("Mango")
print(fruits)

# extending list by adding multiple items at once as list
fruits.extend(["Oranges", "Kiwi", "Melon"])
print(fruits)