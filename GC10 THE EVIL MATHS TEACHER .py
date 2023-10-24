x=0
y=1
print(x)
print(y)
for i in range(99):
    print(x+y)
    i=x
    x=y
    y=i+y
