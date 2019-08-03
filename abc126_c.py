from math import log2, ceil
N, K = map(int, input().split())

proba = 0
for gotvalue in range(1, N + 1):
    if gotvalue < K:
        proba += (0.5**ceil(log2(K / gotvalue))) / N
    else:
        proba += 1 / N
print(proba)
