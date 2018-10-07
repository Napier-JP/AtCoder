N, M, X = map(int, input().split())
#マス0かNに行きたい、M個料金所がある、いまマスXにいる
#問題文が読みづらすぎる
chkptList = list(map(int,input().split()))
TollToOrigin = 0
TollToN = 0
for i in range(X):
    TollToOrigin += chkptList.count(i)
for i in range(X,N):
    TollToN += chkptList.count(i)

print(min(TollToOrigin, TollToN))
