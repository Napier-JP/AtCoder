s = input()
K = int(input())

li = sorted(list(set(s)))
hitList = []

def oneMoreChar(moji):
    hitList.append(moji)
    if len(hitList) < K:
        for i in range(len(li)):
            if moji+li[i] in s:
                return oneMoreChar(moji+li[i])
    else:
        pass

for char in li:
    oneMoreChar(char)

print(hitList[K-1])

