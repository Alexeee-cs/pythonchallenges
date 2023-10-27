#Exercise 1
sentence = input("Enter a sentence: ")
words = sentence.split()
print(words)

#Exercise 2
print((6*1)-2)
print(6*(1-2))

#Exercise 3
#Skip

#Exercise 4
bruce = 6
print(bruce+4)

#Exercise 5
P = 10000
n = 12
r = 0.08
t = int(input("Enter the number of years: "))
A = P*((1+(r/n))**(n*t))
print(A)

#Exercise 6
#Skip

#Exercise 7
time = 14
alarm = 14 + 51
for i in range(10):
    number = 51-(14*i)
    if number < 14:
        break
days = i
addition = 2+(51%14)
if addition > 12:
    addition = addition -12
    print("After",days,"days, at", addition,"am")
else:
    print("After",days,"days, at", addition,"pm")
    
#Exercise 8
current_time = float(input("Enter the current time (in hours, 24-hour format, e.g., 14 for 2 PM): "))
hours_to_wait = 51

try:
    current_time = int(current_time)
    alarm_time = (current_time + hours_to_wait) % 24

    print(f"The alarm goes off at {alarm_time:02}:00")
except ValueError:
    print("Invalid input. Please enter valid integer values for time and hours to wait.")
