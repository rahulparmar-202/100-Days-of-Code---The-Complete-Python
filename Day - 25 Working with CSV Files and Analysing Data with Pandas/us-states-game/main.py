import turtle
import pandas

# Screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
# img contains the path to the image (turtle only runs .gif images)
img = "blank_states_img.gif"
# adding the image to the screen background
screen.addshape(img)
turtle.shape(img)

# reading the csv file and storing into the data variable
data = pandas.read_csv("50_states.csv")

# getting all states in a list format
all_states = data.state.tolist()

# track hoe many user guessed correct
user_guessed = []
# tracks how many states are un-guessed
missing_states = []

game_on = True
while game_on:
    # getting user's input in .title() case (first letter of every word Cap)
    user_answer = screen.textinput(title=f"{len(user_guessed)}/50 Guess the State", prompt="What's another state name?").title()

    if user_answer == "Exit":
        # stores only the states that are not in the user_guessed (both are right)
        """missing_states = [state for state in all_states if state not in user_guessed]"""
        for state in all_states:
            if state not in user_guessed:
                missing_states.append(state)
        # created the data frame of missing_states
        new_data = pandas.DataFrame(missing_states)
        # saved it as a csv file
        new_data.to_csv("states_to_learn.csv", mode="w")
        break

    # if user's input state is in the all_states list
    if user_answer in all_states and user_answer not in user_guessed:
        # extract the row of state guessed
        cor_data = data[data.state == user_answer]
        # created the turtle
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # int(cor_data["x"]) & cor_data.y.item() both are right and contain co-ordination
        t.goto(int(cor_data["x"]), cor_data.y.item())
        t.write(arg=user_answer, move=False, align="center", font=("Arial", 8, "normal"))
        # append the user's guess to the user_guessed list
        user_guessed.append(user_answer)

    else:
        game_on = False

# opening the states_to_learn.csv we created
print(pandas.read_csv("states_to_learn.csv"))