def DefaultLine():
    Line(60)

def Line(Size):
    for Length in range(1, Size + 1):
        print('-')

MySize = int(input("Enter a size:"))

if MySize == -1:
    DefaultLine()
else:
    Line(MySize)
