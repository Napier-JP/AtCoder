N, K = map(int, input().split())
S = input()

# l, r番目以外の人の幸福は変化しない。
# 不幸であるようなl, rを選ぶと左右のグループと結合できて幸福が2増える
# （結合をシミュレートする必要はなく、数だけ減らせばよい）
# 端のグループしか残っていない場合(2グループしかない時)は1増えて操作終了

# run-length
groups = []

nowDirection = S[0]
sameCount = 1
for i in range(1, N):
    if S[i] == nowDirection:
        sameCount += 1
    else:
        groups.append(sameCount)
        nowDirection = S[i]
        sameCount = 1
groups.append(sameCount)

groupCount = len(groups)
ans = sum(groups) - groupCount

for _ in range(K):
    if groupCount >= 3:
        ans += 2
        groupCount -= 2
    elif groupCount == 2:
        ans += 1
        groupCount -= 1
    else:
        break

print(ans)
