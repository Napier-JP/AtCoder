N,C = map(int,input().split())
xLi = []
invXLi = []
vLi = []
invVLi = []
allClock = 0
maxClock = 0
allCounterClock = 0
maxCounterClock = 0
for i in range(N):
    x,v = map(int,input().split())
    xLi.append(x)
    vLi.append(v)
    if i == 0:
        allClock += v-x
    else:
        allClock += v-x+xLi[-2]
    maxClock = max(maxClock, allClock)

invXLi = [C-i for i in xLi[::-1]]
invVLi = vLi[::-1]

for i in range(N):
    if i == 0:
        allCounterClock += invVLi[i]-invXLi[i]
    else:
        allCounterClock += invVLi[i]-invXLi[i]+invXLi[i-1]
    maxCounterClock = max(maxCounterClock, allCounterClock)


print(maxClock)
print(maxCounterClock)
