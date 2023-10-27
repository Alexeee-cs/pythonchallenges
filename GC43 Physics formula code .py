import math
print("Option1: speed distance")
print("Option2: Kinematic energy")
choice = input("Pick the formula you want to use: ")
if choice == '1':
    unknown = input("Enter unknown (speed/distance/time)? ")
    if unknown == 'speed':
        distance = float(input("Enter distance: "))
        time = float(input("Enter time: "))
        speed = round(distance/time,3)
        print("Speed is",speed,("m/s, (3 d.p)"))
    if unknown == 'distance':
        speed = float(input("Enter speed: "))
        time = float(input("Enter time: "))
        distance = round(speed*time,3)
        print("Distance is",distance,("m, (3 d.p)"))
    if unknown == 'time':
        distance = float(input("Enter distance: "))
        speed = float(input("Enter speed: "))
        time = round(distance/speed,3)
        print("Time is",time,("s, (3 d.p)"))
elif choice == '2':
    unknown = input("Enter unknown (KE/mass/velocity)? ")
    if unknown == 'KE':
        mass = float(input("Enter mass: "))
        velocity = float(input("Enter velocity: "))
        KE = round(1/2*mass*velocity**2,3)
        print("KE is",KE,("J, (3 d.p)"))
    if unknown == 'mass':
        KE = float(input("Enter KE: "))
        velocity = float(input("Enter velocity: "))
        mass = round(2*KE/velocity**2,3)
        print("Mass is",mass,("g, (3 d.p)"))
    if unknown == 'velocity':
        KE = float(input("Enter KE: "))
        mass = float(input("Enter mass: "))
        velocity = round(math.sqrt(2*KE/mass),3)
        print("Velocity is",velocity,("m/s, (3 d.p)"))
else:
    print("INVALID INPUT")
