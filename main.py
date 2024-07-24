import turtle
import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("Guess the States in Indian")
screen.setup(width=410, height=467)
image = "India_state.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states_data.csv")
all_states = data.state.to_list()
guess_states = []

while len(guess_states) < 29:
    user_answer = screen.textinput(title=f"{len(guess_states)}/29",
                                   prompt="What's the another state?").title()
    if user_answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guess_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("Learning_States.csv")
        break

    if user_answer in all_states:
        guess_states.append(user_answer)
        deva = turtle.Turtle()
        deva.hideturtle()
        deva.penup()
        state = data[data.state == user_answer]
        deva.goto(int(state.x.item()), int(state.y.item()))
        deva.write(user_answer)

screen.exitonclick()
