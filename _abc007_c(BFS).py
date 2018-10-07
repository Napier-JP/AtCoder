R, C = map(int, input().split())
sy, sx = map(int,input().split())
sy, sx = sy-1, sx-1 #配列のindexとそろえる

gy, gx = map(int, input().split())
gy, gx = gy-1, gx-1 #配列のindexとそろえる

grid = []
distanceGrid = []

searchQueue = [(sy, sx, 0)]

def BFS(row, column, distance):
    if grid[row][column] == "." and distanceGrid[row][column] == -1:
        distanceGrid[row][column] = distance
        searchQueue.append((row+1, column, distance+1))
        searchQueue.append((row-1, column, distance+1))
        searchQueue.append((row, column+1, distance+1))
        searchQueue.append((row, column-1, distance+1))
    else:
        pass
    
for _ in range(R):
    grid.append([char for char in input()])
    distanceGrid.append([-1 for _ in range(C)]) #未探索の座標への距離を-1で初期化

while searchQueue:
    row, col, dist = searchQueue.pop(0)
    BFS(row, col, dist)

print(distanceGrid[gy][gx])
