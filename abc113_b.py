N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
ansIndex = 0
smallestDiff = 999999
for index, height in enumerate(H):
    temp = T - height * 0.006
    diff = abs(A - temp)
    if smallestDiff > diff:
        smallestDiff = diff
        ansIndex = index

print(ansIndex+1)
