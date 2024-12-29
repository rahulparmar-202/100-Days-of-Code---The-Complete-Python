print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    else:
        print("Adult Tickets are $12.")
        bill = 12

    wants_photo = input("do you want a photo taken ? y for Yes and n for No .")
    if wants_photo == "y":
        # add $3 to the bill
        bill += 3

    print(f"Total bill: ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
