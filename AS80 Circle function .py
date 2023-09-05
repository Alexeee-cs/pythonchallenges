import math

def calculate_area(radius):
    area = math.pi * radius**2
    return area

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

radius = int(input("Enter the radius: "))
area = calculate_area(radius)
circumference = calculate_circumference(radius)

print("Area:", area)
print("Circumference:", circumference)
