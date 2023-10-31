def check_string(s):
    vowels = "AEIOUaeiou"
    vowel_count = sum(1 for char in s if char in vowels)
    if vowel_count < 3:
        return False
    
    has_double_letter = any(s[i] == s[i+1] for i in range(len(s) - 1))
    if not has_double_letter:
        return False

    consecutive_letters = any(ord(s[i+1]) - ord(s[i]) == 1 and s[i].isalpha() for i in range(len(s) - 1))
    if consecutive_letters:
        return False

    return True

input_string = input("Enter a string: ")

if check_string(input_string):
    print("String meets the criteria.")
else:
    print("String does not meet the criteria.")
