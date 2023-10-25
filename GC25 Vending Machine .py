Items = ['a','b','c','d','e']
no_   = [1,2,3,4,5]
Price = [1,2,3,4,5]
print(*Items)
print(*no_)
name = int(input("please select the item you want and enter the coresponding number: "))
if name in no_:
    payment = float(input("enter the amount you pay: "))
    if payment > Price[name-1]:
        change = payment - Price[name-1]
        print("You selected",Items[name-1])
        print("Your change will be $",change)
    else:
        print("Not enough for  buying",Items[name-1])
else:
    print("enter a number in the range")
