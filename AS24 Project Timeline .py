from datetime import date
day1_year = int(input("Enter the year of the first time: "))
day1_month = int(input("Enter the month of the first time: "))
day1_date = int(input("Enter the date of the first time: "))
day1_time = date(day1_year, day1_month, day1_date)

day2_year = int(input("Enter the year of the second time: "))
day2_month = int(input("Enter the month of the second time: "))
day2_date = int(input("Enter the date of the second time: "))
day2_time = date(day2_year, day2_month, day2_date)

day_difference = (day2_time) - (day1_time)
print(day_difference.days)
