count = 0
my_byte = str(input("Input your byte:"))
for i in my_byte:
    if i =="1": count = count +1
print(count)

if count%2 == 0: 
    print("Even number of 1s")
else:
    print("Odd number of 1s")



count_1 = 0
count_0 = 0
my_byte = str(input("Input your byte: "))
for i in my_byte:
    if i =="1": 
        count_1 = count_1 +1
    if i =="0":
        count_0 = count_0 +1
type = input("Enter the Parity Check 0/1: ")
if type =="0":
    print(count_0)
    if count_0%2==0:
        print("Even number of 0s")
    else:
        print("Odd number of 0s")
else:
    print(count_1)
    if count_1%2==0:
        print("Even number of 1s")
    else:
        print("Odd number of 1s")
