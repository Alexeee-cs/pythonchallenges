import random
words = ['morning','afternoon','evening','night','midday','midnight']
target = random.choice(words)

attempts = 0
while attempts < 10:
    guess = input("Guess the word: ")
    for letter in target:
        if letter in guess:
            print(letter)
        else:
            print("Wrong guess")
            attempts +1
    if guess == target:
        print("You try",attempts,'times')
        break

print("The word is",target)
