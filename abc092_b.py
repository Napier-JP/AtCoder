n = int(input())
d, x = map(int, input().split())
eaten = x
personList = []
for i in range(n):
    personList.append(int(input()))
    eaten += 1+((d-1) // personList[i])
print(eaten)
