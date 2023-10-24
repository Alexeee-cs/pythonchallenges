earning = int(input("enter the amount of money in ur bank account already: "))
X = int(input("enter the amound u want to withdraw: "))
if X%5 == 0:
    Total = earning - X+0.05
    print("u have $",Total,"remained in ur account")
else:
    print("only accept the transaction if input is a multiple of 5")
