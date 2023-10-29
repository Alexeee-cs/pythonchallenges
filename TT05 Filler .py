import turtle
colors = ["red","orange","yellow","green","blue","purple","pink","brown","gray","black","white"]
 
turtle.penup()
 
turtle.goto(-300,200)
 
for i in range(11):
    turtle.color(colors[i])
    turtle.begin_fill()
    for i in range (3):
        turtle.forward(30)
        turtle.right(120)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
