import sys
N, M = map(int, input().split())

ans = [-1] * (N + 1)  # not evaluated yet

for line in sys.stdin:
    ans[int(line)] = 0  # unreachable

ans[0] = 1  # reachable

if ans[1]:  # if not unreachable
    ans[1] = 1

for i in range(2, N + 1):
    if ans[i]:
        ans[i] = (ans[i - 1] + ans[i - 2]) % 1000000007

print(ans[N])
