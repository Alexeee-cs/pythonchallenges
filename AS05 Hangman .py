import random

wordlist = ["computer", "science", "programming", "python", "challenge"]

def display_word(target, guessed_word):
    display = ""
    for letter in target:
        if letter in guessed_word:
            display += letter
        else:
            display += "_"
    return display

wordlist_pos = random.randint(-1,5)
word_to_guess = wordlist[wordlist_pos]
guessed_word = []
attempts = 10

print("Welcome to Hangman!")
while attempts > 0:
    print(display_word(word_to_guess, guessed_word))
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed_word:
        print("You already guessed that letter.")

    if guess in word_to_guess:
        guessed_word.append(guess)
    else:
        guessed_word.append(guess)
        attempts -= 1
        print("Wrong guess! You have", attempts,"attempts left.")

    if guessed_word == word_to_guess :
        print("Congratulations, you've guessed the word: " + word_to_guess)
        break

    if attempts == 0:
        print("You're out of attempts. The word was: " + word_to_guess)
