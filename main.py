import turtle
import pandas


screen = turtle.Screen()
screen.title("US States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

state_list = data.state.to_list()
game_is_on = True
total_score = 0
guessed_states = []


while game_is_on:

    answer_state = screen.textinput(title=f"{total_score}/50 correct.", prompt="Name a US State").title()

    if answer_state == "Exit":
        break
    if answer_state.title() in state_list and answer_state.title() not in guessed_states:
        answer = turtle.Turtle()
        answer.penup()
        answer.hideturtle()
        row = data[data.state == answer_state.title()]
        x = int(row.x)
        y = int(row.y)
        answer.goto(x, y)
        answer.write(answer_state)
        guessed_states.append(answer_state.title())
        total_score += 1
        if total_score == 50:
            game_is_on = False

missing_states = [state for state in state_list if state not in guessed_states]


df = pandas.DataFrame(missing_states)
df.to_csv("states_to_learn")
