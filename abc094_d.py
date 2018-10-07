#選ぶ場合の、数、じゃなくて選ぶ、場合の数、かよ！また読みづらい問題文を・・・
n = int(input())
li = list(map(int,input().split()))
copied = li.copy()
copied.sort()

ans1 = copied[-1]

ans2 = copied[0]

for i in range(1, n):
    if abs(copied[i] - (ans1 / 2)) < abs(ans2 - (ans1 / 2)):
        ans2 = copied[i]

print("%s %s" %(ans1, ans2))
