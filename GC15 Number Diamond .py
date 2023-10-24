def print_number_diamond(n):
    # Print the top half of the diamond
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        row = spaces + numbers + numbers[-2::-1] + spaces
        print(row)

    # Print the bottom half of the diamond
    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        row = spaces + numbers + numbers[-2::-1] + spaces
        print(row)

n = int(input("number of lines: "))
print_number_diamond(n)
