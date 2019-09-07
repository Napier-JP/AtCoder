N = int(input())
A = [int(i) - 1 for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]


lastEatIdx = -999
ans = 0
for eatIdx in A:
    ans += B[eatIdx]
    if eatIdx == lastEatIdx + 1:
        ans += C[lastEatIdx]
    lastEatIdx = eatIdx

print(ans)
