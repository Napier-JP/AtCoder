N = int(input())
H = list(map(int, input().split()))

ans = 0
lastHeight = H[N - 1]
count = 0
for i in range(N - 1):
    if H[N - i - 2] >= H[N - i - 1]:
        count += 1
        ans = max(ans, count)
    else:
        count = 0

print(ans)
