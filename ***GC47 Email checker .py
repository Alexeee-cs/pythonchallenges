email = input("Enter a email address: ")
separator = "@"  # You can change this to any character or word you want
parts = email.split(separator, 1)
Found = False

if len(parts) == 2:
    part1, part2 = parts
    if element in ('-','.'):
        if any(element in word for word in part1):
            Found = True
    else:
        print(part1)
    if element in ('!','#','$','%','&','*','+','-','/','=','?','^','_','`','{','|','}','~'):
        if any(element in word for word in part2):
            Found = True
    else:
        print(part2)
    print(part2)
else:
    print("Input doesn't contain two parts separated by the chosen delimiter.")

if Found == True:
    print("INVALID")
