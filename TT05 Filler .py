import turtle
colors = ["red","orange","yellow","green","blue","purple","pink","brown","gray","black","white"]
 
turtle.penup()
 
turtle.goto(-300,200)
 
for i in range(11):
    turtle.color(colors[i])
    turtle.begin_fill()
    for i in range (4):
        turtle.forward(30)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(40)
 
turtle.goto(-300,150)
for i in range(11):
    turtle.color(colors[i])
    turtle.write(colors[i])
    turtle.forward(40)
