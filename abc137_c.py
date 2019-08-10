N = int(input())
dic = {}
ans = 0
for _ in range(N):
    si = input()
    sortedSi = "".join(sorted(si))
    if sortedSi in dic:
        dic[sortedSi] += 1
    else:
        dic[sortedSi] = 1

for val in dic.values():
    ans += val * (val - 1) // 2

print(ans)
