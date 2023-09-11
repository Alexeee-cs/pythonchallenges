list1 = [20231.473,15.1414,22518.71]
list2 = [1.8195,126.2574,-14214.532]
list3 = [666666.666666,7.7777777777,8.8888888888888888]

print("Left hand side with one decimal place")
for i in range(3):
    print(f"{list1[i]:<15.1f} {list2[i]:<15.1f} {list3[i]:<15.1f}")

print("\nRight hand side with two decimal points")
for i in range(3):
    print(f"{list1[i]:>15.2f} {list2[i]:>15.2f} {list3[i]:>15.2f}")

print("\nCenter with three decimal points")
for i in range(3):
    print(f"{list1[i]:^15.3f} {list2[i]:^15.3f} {list3[i]:^15.3f}")


number = int(input("Give me a number: "))
print(f"Binary: {number:b}")
