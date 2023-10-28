def whole_number():
    while True:
        user_input = input("Enter a whole number: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a whole number.")

result = whole_number()
print("You entered a whole number:",result)
