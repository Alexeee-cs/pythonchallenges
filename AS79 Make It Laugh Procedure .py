def make_it_laugh(string):
    vowels = 'aeiouAEIOU'
    new_string = ''
    for i in string:
        if i in vowels:
            new_string += '_haha_'
        else:
            new_string += i
    print(new_string)

input_string = input("Enter a string: ")
make_it_laugh(input_string)
