pick_a = int(input("Input any number between 0-12: "))
if 12 < pick_a or pick_a < 0:
    print("INVALID number entered!!!")
else:
    pick_b = int(input("Input any number between 0-12: "))
    if 12 < pick_b or pick_b < 0:
        print("INVALID number entered!!!")
    else:
        answer = pick_a * pick_b
        print(answer)
