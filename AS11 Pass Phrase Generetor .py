import random
number = ['','','','','','','','','','']
password = ''

for i in range(len(number)):
    number[i] = random.randint(0,256)
    password += chr(number[i])

print(password)
