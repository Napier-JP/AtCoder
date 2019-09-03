# cf. https://atcoder.jp/contests/abc139/submissions/7298439
from collections import deque

N = int(input())
A = [deque(a - 1 for a in map(int, input().split())) for _ in range(N)]
matchAvailablePlayers = deque(range(N))  # 対戦可能な状態にある選手リスト 最初は全選手が対戦可能状態
daysPassedWhenPlayedMostRecentMatch = [0] * N  # 各選手が最後の試合を行ったのは何日目か？
desiredOpponentIdx = [-1] * N  # i番目の選手が対戦を希望する相手の番号が[i]に入る

while matchAvailablePlayers:
    playerIdx = matchAvailablePlayers.popleft()
    matchesOrderForThisPlayer = A[playerIdx]  # 鏡像コピー！

    if not matchesOrderForThisPlayer:  # この選手はもう全ての相手と対戦した
        continue

    opponentIdx = matchesOrderForThisPlayer.popleft()  # 対戦したい相手のindex

    if desiredOpponentIdx[opponentIdx] == playerIdx:  # 対戦成立
        daysPassedWhenPlayedMostRecentMatch[playerIdx] = daysPassedWhenPlayedMostRecentMatch[opponentIdx] = max(daysPassedWhenPlayedMostRecentMatch[playerIdx], daysPassedWhenPlayedMostRecentMatch[opponentIdx]) + 1  # 互いの「試合に至った日」をどちらか遅い方に合わせその翌日である今日に書き換える
        matchAvailablePlayers.append(playerIdx)  # 試合終了、対戦可能リストに加える
        matchAvailablePlayers.append(opponentIdx)
    else:  # 相手が自分との対戦を望んでいないので対戦できない、このプレイヤーは対戦待ちをする
        desiredOpponentIdx[playerIdx] = opponentIdx

if any(A):  # リストのリストなので、if A:だと空リストが中に存在しているだけでもTrueになってしまう
    print(-1)
else:
    print(max(daysPassedWhenPlayedMostRecentMatch))
