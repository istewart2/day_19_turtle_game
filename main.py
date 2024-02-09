from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")

turtles = []
colours = ["red", "orange", "yellow", "green", "blue", "purple"]


def create_turtles():
    starting_y_position = -180
    for colour in colours:
        _ = Turtle(shape="turtle")
        _.color(colour)
        _.penup()
        _.goto(-230, starting_y_position)
        starting_y_position += 70
        turtles.append(_)


create_turtles()
race_is_on = True
winning_colour = None

while race_is_on:
    for turtle in turtles:
        distance = random.randint(1, 10)
        turtle.forward(distance)
        position = turtle.xcor()
        if position > 200:
            race_is_on = False
            winning_colour = turtle.pencolor()

if user_bet.lower() == winning_colour:
    print("You win!")
else:
    print(f"You lose.")
print(f"The {winning_colour} turtle won")

screen.exitonclick()
