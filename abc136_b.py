sN = input()
N = int(sN)

ans = 0
for i in range(1, len(sN), 2):
    ans += (10 ** i - 10 ** (i - 1))

if len(sN) % 2 == 1:
    ans += N - 10**(len(sN) - 1) + 1

print(ans)
