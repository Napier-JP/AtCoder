N = int(input())
num = []

ans = 3
plus = 3
while ans <= 10 ** 5:
    num.append(ans)
    ans += plus
    plus += 1

if N in num:
    result = num.index(N)
    print("Yes")
    print(result+2)
    ansGroup = [str(i) for i in range(1, result + 3)]
    for j in range(result + 2):
        print(result + 2, " ".join(ansGroup))
else:
    print("No")
