N = int(input())
v = list(map(int, input().split()))
# 鍋に入れる回数が多いほど寄与度は下がる
v.sort()

ans = 0
for idx, value in enumerate(v):
    if idx == 0 or idx == 1:
        ans += value * 1 / (2 ** (N - 1))
    else:
        ans += value * 1 / (2**(N - idx))
print(ans)
