H, W = map(int, input().split())
grid = []
soloList = []
soloGrid = ""
for _ in range(H):
    row = list(input())
    grid.append(row)

if H == 1 and W == 1:
    if grid[0][0] == ".":
        print("Yes")
    else:
        print("No")

elif H == 1:
    for i in range(H): #行数ぶん繰り返す
        for j in range(W): #列数ぶん繰り返す＝一行当たりのマス数分
            if j == 0:
                if grid[i][j] == "#" and grid[i][j+1] == "." :
                    soloGrid = str(i) + ", " + str(j)
                    soloList.append(soloGrid)
                else:
                    pass
                
            elif j == W-1:
                if grid[i][j] == "#" and grid[i][j-1] == "." :
                    soloGrid = str(i) + ", " + str(j)
                    soloList.append(soloGrid)
                else:
                    pass

            else:
                if grid[i][j] == "#" and grid[i][j-1] == "." and grid[i][j+1] == ".":
                    soloGrid = str(i) + ", " + str(j)
                    soloList.append(soloGrid)
                else:
                    pass
    if soloList == []:
        print("Yes")
    else:
        print("No")

elif W == 1:
    for j in range(W):  #列数ぶん繰り返すが一回だけ
        for i in range(H): #行数ぶん繰り返す＝一列当たりのマス数分
            if i == 0:
                if grid[i][j] == "#" and grid[i+1][j] == "." :
                    soloGrid = str(i) + ", " + str(j)
                    soloList.append(soloGrid)
                else:
                    pass
                
            elif i == H-1:
                if grid[i][j] == "#" and grid[i-1][j] == "." :
                    soloGrid = str(i) + ", " + str(j)
                    soloList.append(soloGrid)
                else:
                    pass
            else:
                if grid[i][j] == "#" and grid[i-1][j] == "." and grid[i+1][j] == ".":
                    soloGrid = str(i) + ", " + str(j)
                    soloList.append(soloGrid)
                else:
                    pass
    print(soloGrid)
    if soloList == []:
        print("Yes")
    else:
        print("No")
                
else:
    for i in range(H): #行数ぶん繰り返す
        for j in range(W): #列数ぶん繰り返す＝一行当たりのマス数分
            if j == 0:
                if grid[i][j] == "#" and grid[i][j+1] == "." :
                    soloGrid = str(i) + ", " + str(j)
                    soloList.append(soloGrid)
                else:
                    pass
                
            elif j == W-1:
                if grid[i][j] == "#" and grid[i][j-1] == "." :
                    soloGrid = str(i) + ", " + str(j)
                    soloList.append(soloGrid)
                else:
                    pass

            else:
                if grid[i][j] == "#" and grid[i][j-1] == "." and grid[i][j+1] == ".":
                    soloGrid = str(i) + ", " + str(j)
                    soloList.append(soloGrid)
                else:
                    pass

#次に縦列で連続しているかチェック
    for j in range(W):  #列数ぶん繰り返す
        for i in range(H): #行数ぶん繰り返す＝一列当たりのマス数分
            if i == 0:
                if grid[i][j] == "#" and grid[i+1][j] == "." :
                    soloGrid = str(i) + ", " + str(j)
                    soloList.append(soloGrid)
                else:
                    pass
                
            elif i == H-1:
                if grid[i][j] == "#" and grid[i-1][j] == "." :
                    soloGrid = str(i) + ", " + str(j)
                    soloList.append(soloGrid)
                else:
                    pass
            else:
                if grid[i][j] == "#" and grid[i-1][j] == "." and grid[i+1][j] == ".":
                    soloGrid = str(i) + ", " + str(j)
                    soloList.append(soloGrid)
                else:
                    pass
            
    if len(soloList) == len(set(soloList)):
        print("Yes")
    else:
        print("No")

