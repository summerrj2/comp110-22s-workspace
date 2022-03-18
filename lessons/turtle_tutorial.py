"""Turtle Tutorial."""

from turtle import Turtle, colormode, done 
leo: Turtle = Turtle()

leo.speed(5)
leo.hideturtle()

side_length: float = 300

i: int = 0 
leo.color("blue")
while i < 3: 
    leo.forward(side_length)
    leo.left(120)
    i = i + 1

leo.penup()
leo.goto(-100, -100)
leo.pendown()
colormode(255)
leo.color(34, 105, 255)

leo.begin_fill()
i: int = 0 
while i < 3: 
    leo.forward(side_length)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()
bob.speed(250)
bob.color(0, 0, 0)
bob.penup()
bob.goto(-100, -100)
bob.pendown()
i: int = 0
while i < 5: 
    bob.forward(300)
    bob.left(123)
    side_length = side_length * .96
    i = i + 1
done()