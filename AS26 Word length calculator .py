with open("counter.txt","r") as whole_file:
    text = whole_file.read()
    words = text.split()
    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)
print(average_length)
