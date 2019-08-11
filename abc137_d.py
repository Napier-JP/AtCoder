# cf. https://atcoder.jp/contests/abc137/submissions/6808061 with some speedup refactoring
import sys
import heapq

N, M = list(map(int, input().split()))
possiblyValidJobs = {}  # 支給が間に合うかもしれない仕事の報酬一覧　支給にkey日かかり、報酬はvalue
for line in sys.stdin:
    A, B = map(int, line.split())
    if A > M:
        continue  # 今から働いても支給が間に合わないのはスルーして次の入力へ

    if A in possiblyValidJobs:  # Aは最大10^5になるのでこの方がdefaultdictより速い
        possiblyValidJobs[A].append(B)
    else:
        possiblyValidJobs[A] = [B]

validJobsOnThisDay = []  # 優先度付きキュー
ans = 0
for daysBeforeDeadline in range(1, M + 1):
    if daysBeforeDeadline in possiblyValidJobs:
        for wage in possiblyValidJobs[daysBeforeDeadline]:
            heapq.heappush(validJobsOnThisDay, -wage)  # heapqは最小のものをheappopするので、最大のものを得たい場合は正負反転が必要
    if validJobsOnThisDay:
        ans += -heapq.heappop(validJobsOnThisDay)  # 「この日やって間に合う仕事の賃金一覧」のうち報酬最大のものを取り出し、正負反転を元に戻す
print(ans)
