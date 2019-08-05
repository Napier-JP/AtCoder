import sys
N, M = map(int, input().split())

Lmax = 1
Rmin = N
for line in sys.stdin:  # much faster than input
    L, R = map(int, line.split())
    Lmax = max(L, Lmax)
    Rmin = min(R, Rmin)

print(max(0, Rmin - Lmax + 1))
