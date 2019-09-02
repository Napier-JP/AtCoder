# cf. https://atcoder.jp/contests/abc139/submissions/7298439
from collections import deque

N = int(input())
A = [[a - 1 for a in map(int, input().split())] for _ in range(N)]
matchAvailablePlayers = deque(range(N))  # 対戦可能な状態にある選手リスト
daysPassedWhenPlayedMostRecentMatch = [0] * N
opponentCandidateIdx = [-1] * N  # i番目の選手が対戦待ちをしている相手の番号が[i]に入る

# 最終日から順に遡る
while matchAvailablePlayers:
    playerIdx = matchAvailablePlayers.popleft()
    matchesOrderForThisPlayer = A[playerIdx]  # 鏡像コピー！

    if not matchesOrderForThisPlayer:  # この選手はもう全ての相手と対戦した
        continue

    finalOpponentIdx = matchesOrderForThisPlayer.pop()  # 現時点で一番最後に対戦したい相手のindex

    if opponentCandidateIdx[finalOpponentIdx] == playerIdx:  # 対戦成立
        daysPassedWhenPlayedMostRecentMatch[playerIdx] = daysPassedWhenPlayedMostRecentMatch[finalOpponentIdx] = max(daysPassedWhenPlayedMostRecentMatch[playerIdx], daysPassedWhenPlayedMostRecentMatch[finalOpponentIdx]) + 1  # 互いの「試合に至った日」をどちらか遅い方に合わせその翌日に書き換える
        matchAvailablePlayers.append(playerIdx)  # 試合終了、対戦可能リストに加える
        matchAvailablePlayers.append(finalOpponentIdx)
    else:  # 対戦できない、このプレイヤーは対戦待ちをする
        opponentCandidateIdx[playerIdx] = finalOpponentIdx

if any(A):  # リストのリストなので、if A:だと空リストが中に存在しているだけでもTrueになってしまう
    print(-1)
else:
    print(max(daysPassedWhenPlayedMostRecentMatch))
