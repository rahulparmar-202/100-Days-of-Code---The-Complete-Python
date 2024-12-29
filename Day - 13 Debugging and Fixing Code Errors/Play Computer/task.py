year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

"""in this code if the year = 1994 then it will not print any of these...
the bug is in the elif and here is the solution :-

    elif year >= 1994:

"""