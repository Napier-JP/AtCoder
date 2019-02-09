N = int(input())
A = []
ans = 0

for _ in range(N):
    A.append(int(input()))

A.sort()
if len(A) % 2 == 1:
    ans += (A[-1] - A[0])
    ans += (A[-2] - A[0])
    A.pop(0)
    while A:
        ans += (A[-1] - A[0])
        A.pop(-1)
        A.pop(0)
else:
    ans += (A[-1] - A[0])
    ans += (A[-2] - A[0])
    A.pop(0)
    while A:
        ans += (A[-1] - A[0])
        A.pop(-1)
        if A:
            ans += (A[-2] - A[0])
            A.pop(0)
        else:
            pass
print(ans)
