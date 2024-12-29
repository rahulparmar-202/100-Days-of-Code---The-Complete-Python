import random
from game_data import data
from art import logo,vs

def answer(person_1,person_2, current_score):
    if person_1['name'] == person_2['name']:
        person_2 = random.choice(data)

    print(f"Compare A : {person_1['name']} is a {person_1['description']}, from {person_1['country']}")
    print(vs)
    print(f"Against B : {person_2['name']} is a {person_2['description']}, from {person_2['country']}")
    """Takes the users choice A or B"""
    user_choice = input("Type 'A' or 'B' : ")
    compare(user_choice, person_1, person_2, current_score)

"""takes user-choice , person_1 and person_2 then according to users choice tell then if they are right or wrong"""
def compare(u_choice, person_A, person_B, score):
    if u_choice == "A":
        if person_A['follower_count'] > person_B['follower_count']:
            # person_A = person_A
            person_B = random.choice(data)
            score += 1
            print(f"You're right! Current Score: {score}")
            print("\n"*2)
            answer(person_A,person_B, score)

        elif person_A['follower_count'] < person_B['follower_count']:
            print("Sorry that's not right!")
            play_game(input("Play Again? Type 'y' or 'n' : "))
        else:
            print("Enter a valid choice.")

    elif u_choice == "B":
        if person_B['follower_count'] > person_A['follower_count']:
            # if user is right, then the next person_A will be person_B and person_B will be random
            person_A = person_B
            person_B = random.choice(data)
            score += 1
            print(f"You're right! Current Score: {score}")
            print("\n"*2)
            answer(person_A,person_B, score)

        elif person_A['follower_count'] > person_B['follower_count']:
            print("Sorry that's not right!")
            play_game(input("Play Again? Type 'y' or 'n' : "))

        else:
            print("Enter a valid choice.")

def play_game(y_n):
    if y_n == "y":
        print(logo)
        """Generate a random integer and find the data for that int as an index"""
        # person_1 = data[random.randint(0, len(data))]
        # person_2 = data[random.randint(0, len(data))]
        person_1 = random.choice(data)
        person_2 = random.choice(data)
        current_score = 0

        answer(person_1, person_2, current_score)

    else:
        return

play_game(input("Start the Game? Type 'y' or 'n': "))
