import turtle
import pandas

def fix_guess(guess:str):
    new_guess =""
    guess_list = guess.split(" ")
    for word in guess_list:
        new_guess += word[0].upper() + word[1:] + " "

    return new_guess[:-1]


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
numb_guessed_states = 0

"""getting variables out of data"""
states_data = pandas.read_csv("50_states.csv")
states_list = states_data["state"].to_list()




print(states_list)

screen.addshape(image)
turtle.shape(image)

"""set up writer"""
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.speed("fastest")

while numb_guessed_states < 50:
    """make sure that the answer goes even if not with capital"""
    answer_state = screen.textinput(title=f"{numb_guessed_states}/50 Guess state",prompt= "Enter a state's name").lower()
    answer_state = fix_guess(answer_state)
    print(answer_state)

    """catch answer """
    if answer_state == "Exit":
        break
    if answer_state in states_list:
        states_list.remove(answer_state)
        numb_guessed_states += 1

        """create a dictionary for the line of the answer"""
        answer_row = states_data[states_data.loc[:,"state"] == answer_state]
        answer_dict = answer_row.iloc[0].to_dict()
        writer.goto(x=answer_dict['x'],y=answer_dict['y'])
        writer.write(arg=f"{answer_state}")




screen.exitonclick()


educational_dict = {"statest to learn":states_list}
educational_table = pandas.DataFrame(educational_dict)
print(educational_dict)
print(educational_table)
