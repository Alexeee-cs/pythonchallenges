playerlist = []
def load_players():
    try:
        with open ("Wrexham.txt") as f:
            for line in f:
                playerlist.append(line.strip())
    except OSError:
        print("File not found")
load_players()
pick = int(input("Enter a number from the range 1 to 28: "))
communityinvolvement = int(input("Enter the change in community involvement: "))
injury = input("Is he injured? (t/f) ")
class wrexham():
    def __init__(self):
        self.__Playernumber = 0
        self.__Forename = ""
        self.__Surname = ""
        self.__Position = ""
        self.__CommunityInvolvement = 0
        self.__Injured = ""
    def Constructor(self):
        self.__Playernumber = playerlist[4*pick]
        self.__Forename = playerlist[4*pick+1]
        self.__Surname = playerlist[4*pick+2]
        self.__Position = playerlist[4*pick+3]
    def ChangeCommunityInvolvement(self):
        self.__CommunityInvolvement = communityinvolvement
    def ChangeInjured(self):
        if injury == 't':
            self.__Injured = 'TRUE'
        elif injury == 'f':
            self.__Injured = 'FALSE'
        else:
            self.__Injured = "Not given"
    def getter(self):
        return self.__Playernumber, self.__Forename, self.__Surname, self.__Position, self.__CommunityInvolvement, self.__Injured

player = wrexham()
player.Constructor()
player.ChangeCommunityInvolvement()
player.ChangeInjured()
print(player.getter())
