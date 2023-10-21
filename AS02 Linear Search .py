def search(list,target):
    for i in range(len(list)):
      if list[i] == target:
        return i
    return False

list = [5,8,4,6,9,2]
target = int(input("Please input your target number: "))
position = search(list,target)

if position!=False:
   print("Found at position",position)
else:
   print("Not Found")
