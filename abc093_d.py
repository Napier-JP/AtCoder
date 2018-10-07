import math
Q = int(input())

for i in range(Q):
    A, B = map(int,input().split())
    if (math.sqrt(A*B))%1 == 0:
        if A == 1 or B==1:
            print(int(math.sqrt(A*B)-1) * 2 - 1)
        else:
            print(int(math.sqrt(A*B)-1) * 2)
    else:
        if abs(A-B) == 1:
            print(int(math.sqrt(A*B)-1) * 2)
        else:
            print(int(math.sqrt(A*B)) * 2 - 1)
