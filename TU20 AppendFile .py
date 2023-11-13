with open("counter.txt","r") as whole_file:
    for line in whole_file:
        maximum = line
maximum = int(maximum)

with open("counter.txt","a") as existing_file:
    for i in range(maximum+1,maximum+11):
        line_to_write = str(i)+"\n"
        existing_file.write(line_to_write)
