
"""
Program Requirements ->

1. Print report.
2. Check resources sufficient?
3. Process coins.
4. Check transaction successful?
5. Make Coffee.

"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
total_profit = 0

def check_ingredients(coffee_ingredients):
    """takes coffee ingredients and check if resource have the ingredients or not and return True and False"""
    for item in coffee_ingredients:
        if coffee_ingredients[item] > resources[item]:
            print(f"Sorry not enough {item} in the Machine.")
            return False
    return True

def take_payment():
    """Takes the payments in Quarter, Dime, Nickle and penny, then return the total """
    print("Payments here ... ")
    total_payment = int(input("Enter Quarter : ")) * 0.25
    total_payment += int(input("Enter Dimes : ")) * 0.1
    total_payment += int(input("Enter Nickle : ")) * 0.05
    total_payment += int(input("Enter Pennies : ")) * 0.01
    return total_payment

def transaction_check(user_total, coffee_price):
    """checks if the user payment is enough or not enough and if is higher than return the change and also calculate the profit"""
    if user_total > coffee_price:
        user_change = round(user_total - coffee_price, 2)
        print(f"Here's your change : ${user_change}")
        global total_profit
        total_profit += coffee_price
        return True
    elif user_total == coffee_price:
        """if the user enters exact amount then ->"""
        print("You payed Exact amount, No change remaining...")
        # global total_profit
        total_profit += coffee_price
        return True
    else:
        print("That's not enough money, Money Refunded!")
        return False

def make_coffee(coffee_name, ingredients):
    """takes the coffee_ingredients and minus them from resources to make coffee."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {coffee_name}🧋.")


game_is_on = True

while game_is_on:
    print("\nMenu : espresso ($1.5) \tlatte ($2.5) \tcappuccino ($3.0)")
    user_choice = input("What drink would you take? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        game_is_on = False
    elif user_choice == "report":
        print("Report : ")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Profit: ${total_profit}")
    else:
        coffee = MENU[user_choice]
        if check_ingredients(coffee['ingredients']):
            payment = take_payment()
            if transaction_check(payment, coffee['cost']):
                make_coffee(user_choice, coffee['ingredients'] )
