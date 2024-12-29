import random
import art
def deal_card():
    """Returns a random card from the cards list"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes a list as parameter and then calculate the score and return it"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw.😒"
    elif c_score == 0:
        return "You Lose. Computer have BlackJack!🤦‍♂️"
    elif u_score == 0:
        return "You Wins with BlackJack! 😊"
    elif u_score > 21:
        return "You Lose, Went over 21.🤦‍♂️"
    elif c_score > 21:
        return "Computer went Over 21, You Win.✌️"
    elif u_score > c_score:
        return "Your score is higher, You Win!😊"
    elif c_score > u_score:
        return "Computer's score is higher, You Lose!🤦‍♂️"
    else :
        return "You Lose.🥲"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"🤠 Your cards: {user_cards}, current score: {user_score}")
        print(f"🤖 Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else :
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"🤠 Your final cards: {user_cards}, final score: {user_score}")
    print(f"🤖 Computer's final cards: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Want to Play a game of BlackJack? Type 'y' or 'n': ") == "y":
    print("\n"*4)
    play_game()