class CutestCat():
    def __init__(self, Name, Description, Weight, Colour, Length, LifeExpectancy, ImageURL):
        self.__Name = Name
        self.__Description = Description
        self.__Weight = Weight
        self.__Colour = Colour
        self.__Length = Length
        self.__LifeExpectancy = LifeExpectancy
        self.__ImageUrl = ImageURL
    def GetCatDetails(self):
        return self.__Name, self.__Description, self.__Weight, self.__Colour, self.__Length, self.__ImageUrl
    def GetCatLife(self):
        return self.__Name, self.__LifeExpectancy
catlist = []
def get_cat():
    try:
        with open ("CutestCats.txt") as f:
            count = 0
            for line in f: #0 is Name, 1 is Description, 2 is Weight, 4 is Length, 6 is colour, 8 is life, 10 is image, 12 is next cat
                if count % 12 == 0:
                    Name = line.strip()
                elif count % 12 == 1:
                    Description = line.strip()
                elif count % 12 == 2:
                    Weight = line.strip()
                elif count % 12 == 4:
                    Length = line.strip()
                elif count % 12 == 6:
                    Colour = line.strip()
                elif count % 12 == 8:
                    LifeExpectancy = line.strip()
                elif count % 12 == 10:
                    ImageURL = line.strip()
                    catlist.append(CutestCat(Name,Description,Weight,Length,Colour,LifeExpectancy,ImageURL))
                count += 1
    except OSError:
        print("File not found")
get_cat()
num = int(input("Enter the car number 1-5: "))
if num > 0 and num < 6:
    ins = int(input("You want all the details(1) or just the life expectancy(2)? "))
    if ins == 1:
        print(catlist[num-1].GetCatDetails())
    elif ins == 2:
        print(catlist[num-1].GetCatLife())
    else:
        print("Not found")
