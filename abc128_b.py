N = int(input())
ans = []
for idx in range(1, N + 1):  # N = 100, no need to use sys.stdin
    S, P = input().split()
    ans.append((S, int(P), idx))

ans.sort(key=lambda x: (x[0], -x[1]))
for unit in ans:
    print(unit[2])
