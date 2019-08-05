r, D, x2k0 = map(int, input().split())
ans = x2k0
for i in range(1, 11):
    ans = r * ans - D
    print(ans)
