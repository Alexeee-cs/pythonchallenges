import turtle
turtle.goto(0,0)
turtle.left(90)
turtle.forward(200)
turtle.write('y')
turtle.goto(0,0)
turtle.right(90)
turtle.forward(450)
turtle.write('x')
turtle.left(180)


for i in range (1,5):
    turtle.goto(100*i,0)
    for n in range(4):
        turtle.forward(50)
        turtle.right(90)
