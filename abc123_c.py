import math
N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
inputs = [A, B, C, D, E]
howManyTimes = []
for num in inputs:
    howManyTimes.append(math.ceil(N / num))
bottleneck = howManyTimes.index(max(howManyTimes))

print(4 + howManyTimes[bottleneck])
