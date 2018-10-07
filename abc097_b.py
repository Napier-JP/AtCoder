import math
X = int(input())
maximumList = []

#32^2=1024なので、2～31までで試せばいい

if X <= 3:
    print(1)
else:    
    for b in range(2,math.ceil(X**0.5)):
        p = 2
        while b**p <= X:
            p += 1
        else:
            if b**(p-1) <= X:
                maximumList.append(b**(p-1))
    print(max(maximumList))
    
