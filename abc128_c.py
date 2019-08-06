N, M = map(int, input().split())

linkedSwitch = []  # index is bulb number, element is list of switches connected to it

for _ in range(1, M + 1):
    s = list(map(lambda x: int(x) - 1, input().split()))[1:]  # k is not necessary
    linkedSwitch.append(s)
p = list(map(int, input().split()))

# (2^N)*Mが余裕で間に合うのでbit全探索する

ans = 0

for i in range(2 ** N):
    switchStatus = bin(i)[2:].zfill(N)

    for bulbIndex in range(M):
        onCount = 0

        for switchIndex in linkedSwitch[bulbIndex]:
            onCount += int(switchStatus[switchIndex])

        if onCount % 2 != p[bulbIndex]:  # Mission failed. we'll get'em next time.
            break
    else:  # All bulbs are lit
        ans += 1

print(ans)
