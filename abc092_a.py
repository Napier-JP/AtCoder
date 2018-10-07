a=input()
b=input()
c=input()
d=input()

a=int(a)
b=int(b)
c=int(c)
d=int(d)

if a > b:
    if c > d:
        print(b+d)
    else:
        print(b+c)
else:
    if c > d:
        print(a+d)
    else:
        print(a+c)
