import turtle 
n = int(input("Enter the no of the sides of the polygon : ")) 
l = int(input("Enter the length of the sides of the polygon : ")) 

for i in range(n):
    turtle.forward(l) 
    turtle.right((360 / n))
