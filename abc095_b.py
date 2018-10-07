N, X = map(int,input().split())
m = 0
smallest = 0
total = 0

for i in range(N):
    m =int(input())
    total += m
    if smallest == 0 or m < smallest:
        smallest = m
    else:
        pass


print(N + (X-total)//smallest)
    
