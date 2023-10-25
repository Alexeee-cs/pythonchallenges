gender = input('enter your gender: ')
if gender in ('m','M','male','Male','MALE'):
    need = 2500
else:
    need = 2000
name = input("name of the diet: ")
while name != 'end day':
    calories = float(input("calories of the food: "))
    print("You still need:",(need-calories))
    name = input("name of the diet: ")
