L = list(map(int,input().split()))
L.sort()

if (L[-1]-L[0])%2 + (L[-1]-L[1])%2 == 2:
    print((L[-1]-L[0])//2 + (L[-1]-L[1])//2 + 1)
elif (L[-1]-L[0])%2 + (L[-1]-L[1])%2 == 1:
    print((L[-1]-L[0])//2 + (L[-1]-L[1])//2 + 2)
else:
    print((L[-1]-L[0])//2 + (L[-1]-L[1])//2)
