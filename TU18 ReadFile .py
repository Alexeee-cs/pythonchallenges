from time import sleep
choice = input("Choose your poem (rudyard/mam): ").lower()
if choice == 'rudyard':
    with open("rudyard.txt","r") as whole_file:
        for line in whole_file:
            print(line,end="")
            sleep(0.5)
elif choice == 'mam':
    with open("mam.txt","r") as whole_file:
        for line in whole_file:
            print(line,end="")
            sleep(0.5)
else:
    print("INVALID")
