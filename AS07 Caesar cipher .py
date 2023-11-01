sentence = input("Enter a string: ")
new_sentence = ''
for char in sentence.lower():
    if ord(char) == 32:
        new_char = 32
    else:
        new_char = ord(char) + 10
        if new_char >= 122:
            temp = new_char - 122
            new_char = 97 + temp
    new_sentence += chr(new_char)

print(new_sentence)
