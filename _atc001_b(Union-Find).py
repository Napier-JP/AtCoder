N, Q = map(int,input().split()) #要素数、クエリ数

parent = [i for i in range(N)]  #配列のi番目の要素の親は最初はすべてi（自身）

def root(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = root(parent[x]) #根に直接つなぎなおす
        return parent[x]
    
def isReachable(x, y):
    return root(x) == root(y)

def unite(x, y):
    if root(x) == root(y):
        pass
    else:
        parent[x] = y

for i in range(Q):
    P, A, B = map(int, input().split())
    if P == 0:
        unite(A, B)
    else:
        ans = "Yes" if isReachable(A,B) else "No"
        print(ans)

