N, Q = map(int, input().split())
nodes = [[-1, set()] for _ in range(N + 1)]  # (親node、set(子nodes))
nodes[1][0] = 1  # 1の親は1
ans = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())  # 接続ノード
    nodes[a][1].add(b)  # aの子にb

searchTargets = []
for childIdx in nodes[1][1]:
    searchTargets.append((1, childIdx))  # 親ノード番号, 探索先ノード番号

while searchTargets:
    parentIdx, targetIdx = searchTargets.pop()
    nodes[targetIdx][0] = parentIdx
    nodes[nodes[parentIdx][0]][1].add(targetIdx)
    for childIdx in nodes[targetIdx][1]:
        searchTargets.append((targetIdx, childIdx))

for _ in range(Q):
    p, x = map(int, input().split())
    ans[p] += x
    for descendant in nodes[p][1]:
        ans[descendant] += x
ans.pop(0)
print(" ".join(map(str, ans)))
