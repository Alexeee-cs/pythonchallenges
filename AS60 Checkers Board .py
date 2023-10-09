def create_checkerboard(n, m):
    checkerboard = []

    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 2 == 0:
                row.append(".")
            else:
                row.append("*")
        checkerboard.append(row)

    return checkerboard

n = int(input("Give me number of rows: "))
m = int(input("Give me number of columns: "))

checkerboard = create_checkerboard(n, m)

for i in range (m):
    print(*checkerboard[i-1])
