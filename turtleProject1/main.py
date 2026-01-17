from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=300, height=300)
timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.penup()  # Ensure the turtle doesn't draw a line when moving
timmy.goto(0, 0)  # Move the turtle to the center of the screen

screen = Screen()
screen.exitonclick()