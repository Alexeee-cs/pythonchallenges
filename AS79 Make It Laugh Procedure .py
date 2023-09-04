def make_it_laugh(string):
    vowels = 'aeiouAEIOU'
    modified_string = ''
    for char in string:
        if char in vowels:
            modified_string += ' haha '
        else:
            modified_string += char
    print(modified_string)

input_string = input("Enter a string: ")
make_it_laugh(input_string)
