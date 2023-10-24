import random
target = random.randint(0,100)
print(target)
for i in range(1000):
    guess = int(input("Please guess a number: "))
    if guess > target:
        if guess > 100:
            print("     Please guess a number between 1-100 \n")
        else:
            print("     Your guess is OVER the target \n")
    elif guess < target:
        print("     Your guess is FEWER than the target \n")
    else:
        print("You get it!")
        break
