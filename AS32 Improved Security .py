import random
numoffloor = int(input("Enter the number of floor: "))
listn=[]
for i in range(1,numoffloor+1):
    listn.append(i)
for i in range(len(listn)):
    level = random.randint(1,len(listn))
    print("The floor you will go is:",listn[level-1])
    listn.pop(level-1)
    print(listn)
