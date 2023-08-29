import random
mynumber = random.uniform(0.1, 9.9)
New_number = round(mynumber,3)
print(New_number)


import random
Choose_Name = ["James","John","Mark","Rick"]
for i in range (1,6):
  chosen = random.choice(Choose_Name)
  print(chosen)
  choice = input("Do you want to remove the name? ")
  if choice == ["y,Y,yes,Yes,YES"]:
    Choose_Name.remove(chosen)
  else:
    print(" ")
