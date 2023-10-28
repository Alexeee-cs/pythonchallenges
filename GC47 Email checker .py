email = input("Enter a email address: ")
separator = "@"
parts = email.split(separator, 1)
if len(parts) == 2:
    part1,part2 = email.split(separator, 1)
    Found = False
    if len(part1) > 64 or len(part2) > 253:
        Found = True

    element_1 = ['-','.']
    for element in element_1:
        if element in part1:
            Found = True

    element_2 = ['!','#','$','%','&','*','+','-','/','=','?','^','_','`','{','|','}','~']
    for element in element_2:
        if element in part2:
            Found = True

    if Found == True:
        print("INVALID")
    else:
        print("Personal_info part:",part1)
        print("Domain name:",part2)
else:
    print("Input doesn't contain two parts separated by the chosen delimiter.")
