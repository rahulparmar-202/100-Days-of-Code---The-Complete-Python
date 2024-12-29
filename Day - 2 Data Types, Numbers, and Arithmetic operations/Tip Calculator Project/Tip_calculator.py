print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 (%): "))
people = int(input("How many people to split the bill? "))

tip_amount = (tip / 100) * bill
total_bill = bill + tip_amount
split = total_bill / people

print(f"Each Person should Pay: {split}")

