N = int(input())
S = input()

maxCount = 0

if N == 2:
    print(len(set(S[0])&set(S[-1])))
else:
    for i in range(N):
        commonCount = len(set(S[0:i+1])&set(S[i+1:]))
        if maxCount < commonCount:
            maxCount = commonCount
    print(maxCount)

