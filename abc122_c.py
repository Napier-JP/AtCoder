N, Q = map(int, input().split())
S = input()
count = 0
counts = [0 for _ in range(N)]

for i in range(N - 1):
    if S[i] == "A" and S[i + 1] == "C":
        count += 1
        counts[i + 1] = count
    else:
        counts[i + 1] = count

for _ in range(Q):
    li, ri = map(int, input().split())
    print(counts[ri - 1] - counts[li - 1])
