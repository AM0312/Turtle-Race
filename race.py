from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(
    title="Make your bet", prompt="Which turtle will win? Enter color:")

colors = ["red", "orange", "yellow", "green", "blue", "violet"]
y = [-100, -60, -20, 20, 60, 100]
turtles = []

for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-225, y=y[i])
    turtles.append(t)

game_on = False
if user_choice:
    game_on = True
while game_on:
    for turtle in turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() > 230:
            game_on = False
            winning = turtle.pencolor()

if winning == user_choice:
    print(f"Congrats {winning} won")
else:
    print(f"You lose, {winning} won.")

screen.exitonclick()
