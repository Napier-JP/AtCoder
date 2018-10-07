N, M = map(int,input().split())

#小さい数字から順番に探索していく。一度通ったところはフラグ1を立てる。
#もし探索の途中ですでにフラグ1であるところに到達したら、その連結成分は木ではない。
#これをフラグが0であるものについて繰り返し行う。

isVisited = [0 for _ in range(N)] #最初はすべて未訪問
isVisited.insert(0, None) #頂点のindexをそろえる

edge = [[] for _ in range(N)]
edge.insert(0, None) #頂点のindexをそろえる

treeCount = 0

def DFS(num):
    stack = [num]
    isTree = True
    
    while stack:
        vertex = stack.pop()
        if isVisited[vertex] == 0: #未訪問なら訪問して繋がっている頂点をスタックに入れる
            isVisited[vertex] = 1
            stack.extend(edge[vertex])
        else: #訪問済みなので、フラグを立てる必要もないし、繋がっている頂点はもう把握している
            isTree = False

    return isTree
        
    
for _ in range(M): #入力処理
    u, v = map(int, input().split())
    edge[u].append(v)

for i in range(1,N+1): #すべての頂点について（未訪問なら）DFSしていき、木ならカウントを1ふやす
    if isVisited[i] == 0:
        treeCount += (DFS(i))
    else:
        pass

print(treeCount)
