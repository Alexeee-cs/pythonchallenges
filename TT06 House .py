import turtle
colors = ["red","brown"]

turtle.penup()
 
turtle.goto(-300,200)
 
turtle.color(colors[0])
turtle.begin_fill()
for i in range (3):
    turtle.right(120)
    turtle.forward(30)
turtle.end_fill()
turtle.penup()
turtle.right(120)
turtle.forward(30)
turtle.right(120)
turtle.forward(30)
turtle.pendown()
turtle.color(colors[1])
turtle.begin_fill()
for i in range(4):
    turtle.left(90)
    turtle.forward(30)
turtle.end_fill()
