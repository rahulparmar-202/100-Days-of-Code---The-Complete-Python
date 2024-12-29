# You can put if/else statements inside other if/else statements. This is known as nesting. e.g.



print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Enter Age : "))
    if age <= 12:
        print("Please Pay $5")
    elif age > 12 and age < 18 :
        print("Pay $7")
    else :
        print("Pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")
