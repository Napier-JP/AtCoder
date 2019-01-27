N, A, B = map(int, input().split())
maxAns = min(A, B)
minAns = max(0, A+B-N)

print(maxAns, minAns)
