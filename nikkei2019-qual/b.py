N = int(input())
A = input()
B = input()
C = input()

ans = 0

for i in range(N):
    chars = set()
    chars.add(A[i])
    chars.add(B[i])
    chars.add(C[i])
    ans += len(chars)-1

print(ans)
