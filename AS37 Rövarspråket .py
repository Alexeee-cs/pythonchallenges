def secret_language(string):
    vowels = 'aeiouAEIOU'
    new_string = ''
    for i in string:
        if i in vowels:
            new_string += i
        else:
            new_string += i+'o'+i
    print(new_string)

input_string = input("Enter a string: ")
secret_language(input_string)
