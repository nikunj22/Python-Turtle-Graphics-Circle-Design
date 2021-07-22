import turtle
turtle.bgcolor("blue")

turtle.pensize(10)
turtle.speed(0)
for i in range(10):
    for colours in['red','green','yellow','white','blue']:
        turtle.color(colours)
        turtle.circle(50)
        turtle.left(10)
turtle.hideturtle()