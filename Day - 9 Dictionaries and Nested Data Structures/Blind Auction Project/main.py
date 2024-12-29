# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

# from art import logo
# print(logo)

import art
print(art.logo)


# function that compares the bids and find the highest one.
def find_highest_bidder(bidding_dictionary):
    winner = ""
    current_highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > current_highest_bid:
            current_highest_bid = bid_amount
            winner = bidder

    print(f"The Winner is {winner} with a bid of ${current_highest_bid}.")


# while loop that runs until the user enters no
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("Enter your name : ")
    price = int(input("What's your bid : $"))
    bids[name] = price
    new_bids = input("Are there any ohter bidders? Type 'yes' or 'no' .").lower()
    if new_bids == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif new_bids == "yes":
        print("\n" * 20)
        continue_bidding = True


