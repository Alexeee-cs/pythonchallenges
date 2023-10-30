sentence = input("Enter a string: ")
new_sentence = ''
for char in sentence:
    new_char = ord(char) +1
    if new_char == 33:
        new_char = 32
    new_sentence += chr(new_char)

print(new_sentence)
