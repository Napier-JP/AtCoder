# can't AC without numpy, Python array handling with for is SLOW
import sys
H, W = map(int, input().split())
S = [line.strip("\n") for line in sys.stdin]

# i行j列に置いたとき上下左右の方向それぞれに光の軌跡が何マス伸びるか(自マスを含む)
trailLeft = [[0] * W for _ in range(H)]
trailRight = [[0] * W for _ in range(H)]
trailUp = [[0] * W for _ in range(H)]
trailDown = [[0] * W for _ in range(H)]

for i in range(H):  # 各行について下に見ていく
    for j in range(W):  # その行の各列について右に見ていく
        if S[i][j] == '#':
            pass  # そのマスに置いたとき照らすのは0マス(置けないので)
        else:
            if i == 0 and j == 0:  # 左上
                trailLeft[i][j] = 1
                trailUp[i][j] = 1
            elif i == 0:  # 最上行
                trailLeft[i][j] = trailLeft[i][j - 1] + 1
                trailUp[i][j] = 1
            elif j == 0:  # 最左列
                trailLeft[i][j] = 1
                trailUp[i][j] = trailUp[i - 1][j] + 1
            else:
                trailLeft[i][j] = trailLeft[i][j - 1] + 1
                trailUp[i][j] = trailUp[i - 1][j] + 1

        k = H - i - 1  # H-1 to 0
        l = W - j - 1  # W-1 to 0
        # 左上に見ていく
        if S[k][l] == "#":
            pass
        else:
            if k == H - 1 and l == W - 1:  # 右下
                trailRight[k][l] = 1
                trailDown[k][l] = 1
            elif k == H - 1:  # 最下行
                trailRight[k][l] = trailRight[k][l + 1] + 1
                trailDown[k][l] = 1
            elif l == W - 1:  # 最右列
                trailRight[k][l] = 1
                trailDown[k][l] = trailDown[k + 1][l] + 1
            else:
                trailRight[k][l] = trailRight[k][l + 1] + 1
                trailDown[k][l] = trailDown[k + 1][l] + 1

ans = 0

for i in range(H):  # 各行について下に見ていく
    for j in range(W):  # その行の各列について右に見ていく
        ans = max(ans, trailLeft[i][j] + trailRight[i][j] + trailUp[i][j] + trailDown[i][j] - 3)

print(ans)
