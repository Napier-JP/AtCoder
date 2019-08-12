# can't AC without numpy, Python array handling with for is SLOW
import numpy as np
H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(input()))
S = (np.array(S) == ".") * 1

# i行j列に置いたとき上下左右の方向それぞれに光の軌跡が何マス伸びるか(自マスを含む)
trailLeft = np.zeros((H, W), dtype=int)
trailRight = np.zeros((H, W), dtype=int)
trailUp = np.zeros((H, W), dtype=int)
trailDown = np.zeros((H, W), dtype=int)

for i in range(H):
    if i == 0:
        trailUp[i] = S[i]
        trailDown[H - i - 1] = S[H - i - 1] * 1
    else:
        trailUp[i] = (trailUp[i - 1] + 1) * S[i]
        trailDown[H - i - 1] = (trailDown[H - i] + 1) * S[H - i - 1]

for j in range(W):
    if j == 0:
        trailLeft[:, j] = S[:, j]
        trailRight[:, W - j - 1] = S[:, W - j - 1] * 1
    else:
        trailLeft[:, j] = (trailLeft[:, j - 1] + 1) * S[:, j]
        trailRight[:, W - j - 1] = (trailRight[:, W - j] + 1) * S[:, W - j - 1]

print(np.max(trailLeft + trailRight + trailUp + trailDown - 3))
