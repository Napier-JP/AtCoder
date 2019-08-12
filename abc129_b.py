N = int(input())
W = list(map(int, input().split()))
total = sum(W)
partial = 0
ans = 10000
for weight in W:
    partial += weight
    ans = min(ans, abs(total - partial * 2))

print(ans)
