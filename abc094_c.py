N = int(input())

li = list(map(int,input().split()))
copiedListForSort = li.copy()
copiedListForSort.sort()

firstMedian = copiedListForSort[N//2 - 1]
secondMedian = copiedListForSort[N//2]
for i in range(N):
    if li[i] >= secondMedian:
        print(firstMedian)
    else:
        print(secondMedian)
