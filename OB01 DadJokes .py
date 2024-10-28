import random
class Jokes():
    def __init__(self):
       self.prompt = ""
       self.answer = ""

jokes = []
def get_jokes():
    try:
        with open ("DadJokes.txt") as f:
            for line in f:
                jokes.append((line).strip())
    except OSError:
        print("Sorry couldn't find the file")

get_jokes()
num = random.randint(0,(len(jokes)//2))
print(jokes[2*num])
response = input("Enter the answer: ")
print(jokes[2*num+1])
