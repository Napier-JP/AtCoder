S = input()
trapLeftSideIndices = []
traps = []
ans = [0] * len(S)

count = [0, 0]
for idx, char in enumerate(S):
    if char == "R" and count[1] == 0:
        count[0] += 1
    elif char == "R":
        traps.append(count)
        count = [1, 0]
    elif char == "L" and count[1] == 0:
        trapLeftSideIndices.append(idx - 1)
        count[1] += 1
    elif char == "L":
        count[1] += 1
else:
    traps.append(count)

for idx, trap in enumerate(traps):
    leftSideNum = (trap[0] - trap[0] // 2) + trap[1] // 2
    rightSideNum = (trap[1] - trap[1] // 2) + trap[0] // 2
    ans[trapLeftSideIndices[idx]] = leftSideNum
    ans[trapLeftSideIndices[idx] + 1] = rightSideNum

print(" ".join(map(str, ans)))
