N = int(input())
a = list(map(int, input().split()))
avg = sum(a) / len(a)
diff = 999

for index, num in enumerate(a):
    if abs(avg - num) < diff:
        diff = abs(avg - num)
        ans = index

print(ans)
