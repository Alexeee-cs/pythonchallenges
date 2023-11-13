with open("rudyard.txt","w") as new_file:
    for i in range(10,-1,-1):
        new_file.write(str(i)+' ')
