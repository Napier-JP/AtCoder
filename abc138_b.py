N = int(input())
A = list(map(int, input().split()))
total = 0
for num in A:
    total += 1 / num

print(1 / total)
