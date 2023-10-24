number = int(input("how many sibilings there are: "))
time = float(input("how many hours can they play: "))
time_person = time / number
if time_person < 1:
    time_person_new = time_person*60
    print("each person can play",round(time_person_new,2),'minutes')
else:
    print("each person can play",round(time_person,2),'hours')
