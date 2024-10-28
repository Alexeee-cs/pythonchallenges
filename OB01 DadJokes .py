import random
jokes = []
def get_jokes():
    try:
        with open ("DadJokes.txt") as f:
            for line in f:
                jokes.append(line.strip())
    except OSError:
        print("Sorry couldn't find the file")

get_jokes()

class Jokes():
    def __init__(self):
       self.__prompt = ""
       self.__answer = ""

    def setter(self):
        num = random.randint(0,10)
        self.__prompt = jokes[2*num]
        self.__answer = jokes[2*num+1]

    def prompt_getter(self):
        return self.__prompt

    def answer_getter(self):
        return self.__answer

joke = Jokes()
joke.setter()
print("Joke:", joke.prompt_getter())
response = input("Your response: ")
print("Answer:", joke.answer_getter())
