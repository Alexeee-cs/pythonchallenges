x=0
y=1
print('0 : ',x)
print('1 : ',y)
for i in range(99):
    print((i+2),':',x+y)
    i=x
    x=y
    y=i+y
