import turtle

instruction = []
def Constructor():
    try:
        with open ("Initialise.txt") as f:
            for line in f:
                instruction.append(line.strip())
    except OSError:
        print("File not found")
Constructor()
pick = int(input("Enter a number from the range 1 to 5: "))
class pattern():
    def __init__(self, angle: int, times: int):
        self.__angle = angle # Integer
        self.__times = times # Integer
    def draw_pattern(self):
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
        turtle.setup(800, 600)  # setting window dimensions
        turtle.bgcolor('black')
        for x in range(self.__times):
            turtle.pencolor(colors[x % 6])
            turtle.width(x / 100 + 1)
            turtle.forward(x)
            turtle.left(self.__angle)
            turtle.speed(0)
        turtle.done()
    def setter(self):
        self.__angle = int(instruction[2*(pick-1)])
        self.__times = int(instruction[2*(pick-1)+1])
    def Constructor(self):
        return self.__angle, self.__times

mypattern = pattern(0,0)
mypattern.setter()
mypattern.draw_pattern()
