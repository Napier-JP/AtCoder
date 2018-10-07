import math
N = int(input())
a = [int(num) for num in input().split()]
count = 0

for i in range(N):
    count += bin(a[i])[::-1].index("1")

print(count)
