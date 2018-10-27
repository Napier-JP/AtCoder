A, B, K = map(int, input().split())

for _ in range(K//2):
    B += A//2
    A = A // 2

    A += B // 2
    B = B // 2

if (K % 2 == 1):
    B += A//2
    A = A // 2

print(A, B)
