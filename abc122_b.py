S = input()
acgt = ["A", "C", "G", "T"]
ans = 0

for i in range(len(S)):
    if S[i] in acgt:
        j = i
        while True:
            if j < len(S) - 1 and S[j + 1] in acgt:
                j += 1
            else:
                break
        ans = max(j - i + 1, ans)

print(ans)
