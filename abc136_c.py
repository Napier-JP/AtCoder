N = int(input())
H = [int(i) for i in input().split()]

lastHeight = 0
for idx in range(len(H)):
    if H[idx] < lastHeight:
        print("No")
        break
    elif H[idx] == lastHeight:
        lastHeight = H[idx]
    else:
        lastHeight = H[idx] - 1
else:
    print("Yes")
