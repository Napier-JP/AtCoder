N, K = map(int, input().split())
a = list(map(int, input().split()))
sums = []
power = 0
ans = 0
powerCount = []

for i in range(len(a)):
    for j in range(i, len(a)):
        sums.append(sum(a[i:j + 1]))

maxNum = max(sums)
while (maxNum > 1):
    maxNum = maxNum / 2
    power += 1
sums.sort()

binary = [format(i, "b").zfill(power) for i in sums]
# 各ビットについて、いくつの数字において1があったかをカウントし、K以上あったものの和が答え

for i in range(power):
    if len([num for num in binary if num[i] == "1"]) >= K:
        ans += 2 ** (power - i - 1)
        binary = [num for num in binary if num[i] == "1"]
    else:
        binary = [num for num in binary if num[i] == "0"]


print(ans)
