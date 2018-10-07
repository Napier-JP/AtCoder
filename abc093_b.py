A, B, K = map(int,input().split())

if (B-A+1) > 2*K:
    for i in range(K):
        print(A+i)
    for j in range(K):
        print(B-K+1+j)
else:
    for m in range(B-A+1):
        print(A+m)
