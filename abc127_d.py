# cf. https://atcoder.jp/contests/abc127/submissions/5568030

import sys

N, M = map(int, input().split())
A = list(map(int, input().split()))
p = [(A[i], 1) for i in range(N)]  # N tuples

for line in sys.stdin:
    B, C = map(int, line.split())
    p.append((C, B))  # add M tuples

p.sort(reverse=True)  # (N+M)log(N+M), sorted by A[i] or C, high to low

ans, remainingCardsToChoose = 0, N
for cardValue, availableCardCount in p:
    chooseCount = min(availableCardCount, remainingCardsToChoose)
    ans += chooseCount * cardValue
    remainingCardsToChoose -= chooseCount

print(ans)
