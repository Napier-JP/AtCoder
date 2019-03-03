A, B, K = map(int, input().split())
div = []
i = 1
while i <= 100:
    if A % i == 0 and B % i == 0:
        div.append(i)
    i += 1
print(div[-K])
