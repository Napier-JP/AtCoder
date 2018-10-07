N, K = map(int, input().split())
A = list(map(int, input().split()))

if (N-K)%(K-1) == 0:
    print(1+(N-K)//(K-1))
else:
    print(1+(N-K)//(K-1)+1)
