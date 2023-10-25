for i in range(1,21):
    if i%3 == 0:
        if i%5 != 0:
            print("Fizz")
        else:
            print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
