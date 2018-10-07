A, B, N=map(int,input().split())
X = input()

for i in range(N):
    if X[i] == "S" and A != 0:
        A = A-1
    elif X[i] == "C" and B != 0:
        B = B-1
    elif X[i] == "E" and (A != 0 or B != 0):
        if A>=B:
            A = A-1
        else:
            B = B-1
print(A)
print(B)
