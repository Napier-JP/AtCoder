H, W = map(int, input().split()) #Height=縦の長さ=行数 Width=横の長さ=列数

grid = []
stack = [] #探索すべき場所
reachable = [[0 for _ in range(W)] for _ in range(H)] #探索済みフラグ(1なら通れる)
start = (0, 0)
goal = (0, 0)

def DFS_stack(x, y): #xは縦の位置、x+1は下。yは横の位置、y+1は右
    if x < 0 or y < 0 or x > H-1 or y > W-1 or grid[x][y] == "#": #マップからはみ出たか通行不能
        pass
    elif reachable[x][y] == 1: #もう見た
        pass
    else:
        reachable[x][y] = 1
        stack.append((x-1, y))
        stack.append((x+1, y))
        stack.append((x, y-1))
        stack.append((x, y+1))

        
for i in range(H):
    grid.append([char for char in input()]) #各行の要素をH行ぶん追加していく
    if "s" in grid[i]:
        start = (i, grid[i].index("s"))
    if "g" in grid[i]:
        goal = (i, grid[i].index("g"))

#print(grid)
#print(start)
#print(goal)

stack.append(start)
while stack:
    x, y = stack.pop()
    DFS_stack(x, y)

if reachable[goal[0]][goal[1]] == 1:
    print("Yes")
else:
    print("No")
