for i in range(100):
    ratio_type = input("Enter either GPM / NPM: ")
    sales = int(input("Enter the number of sales made: "))
    if ratio_type.upper() == 'GPM':
        profit = float(input("Enter the gross profits: "))
        GPM = (profit/sales) * 100
        print("The GPM is",GPM,"%")
        break
    elif ratio_type.upper() == 'NPM':
        profit = float(input("Enter the net profits: "))
        NPM = (profit/sales) * 100
        print("The NPM is",NPM,"%")
        break
    else:
        print("Please enter again")
