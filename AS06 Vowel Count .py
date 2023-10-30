sentence = input("Enter a string: ")
vowels = 'aeiouAEIOU'
number = 0
for i in sentence:
    if i in vowels:
        number = number +1
print("There are",number,'vowels')
