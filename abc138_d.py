N, Q = map(int, input().split())
parentNodes = [1] * (N + 1)  # parentNodes[i] = i番目ノードの親番号

ans = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())  # 接続ノード
    parentNodes[b] = a

for _ in range(Q):
    p, x = map(int, input().split())
    ans[p] += x

for i in range(2, N + 1):
    ans[i] += ans[parentNodes[i]]

ans.pop(0)
print(" ".join(map(str, ans)))
