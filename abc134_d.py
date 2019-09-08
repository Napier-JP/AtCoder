N = int(input())
a = list(map(int, input().split()))
boxes = [0] * N
for i in reversed(range(N)):  # i from N-1 to 0
    boxes[i] = (2 + a[i] - sum(boxes[i::i + 1]) % 2) % 2

ansCount = 0
ansIndices = []
for idx, content in enumerate(boxes):
    if content:
        ansCount += 1
        ansIndices.append(idx + 1)

print(ansCount)
if ansCount > 0:
    print(" ".join(map(str, ansIndices)))
