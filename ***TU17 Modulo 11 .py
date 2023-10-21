new_list = ['','','','']
lst = str(input("Give me four numbers: "))
checksum = int(input("Enter the checksum: "))
#step 3
for i in range(len(lst)):
    new_list[i] = int(lst[i])*(i+1)
#step 4
sum_list = sum(new_list)
#step 5
modulo_11 = sum_list%11
#step 6
answer = 11-modulo_11
print("The checksum we get is",answer)
#check the answer
if answer == checksum:
    print("TRUE")
else:
    print("FALSE")
