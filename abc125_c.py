# naive solution
N = int(input())
A = [int(i) for i in input().split()]

# GCDは最小の数に制約を受ける
A.sort()


def euclidian(A, B):
    A = A % B
    if A == 0:
        return B
    else:
        return euclidian(B, A)


if N == 2:
    print(max(A[0], A[1]))
else:
    firstGCD = 10e+9
    for other in A[2:]:
        firstGCD = min(firstGCD, euclidian(other, A[0]))

    secondGCD = 10e+9
    A.pop(1)
    for other in A[1:]:
        secondGCD = min(secondGCD, euclidian(other, A[0]))

    print(max(firstGCD, secondGCD))
