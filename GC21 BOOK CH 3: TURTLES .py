#Exercise 1
print("We like python's turtles\n" * 10)
#Exercise 2
#def make_call(phone_number):
#def send_text_message(recipient, message_content):
#def check_battery_status():
#Exercise 3
months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
for i in range (12):
    print("One of the month in a year is",months[i])
#Exercise 4
45 degrees
#Exercise 5
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in range(len(xs)):
    print(xs[i])
for i in range(len(xs)):
    print(xs[i],(xs[i])**2,sep=',')
print(sum(xs))
def multiply_list(xs):
    tot = 1
    for x in xs:
        tot *= x
    return tot
print(multiply_list(xs))
