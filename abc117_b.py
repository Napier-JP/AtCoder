N = int(input())
L = list(map(int, input().split()))
total = sum(L)
isOK = True

for num in L:
    if num * 2 < total:
        pass
    else:
        isOK = False

if isOK:
    print("Yes")
else:
    print("No")
