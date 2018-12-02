S = input()
smallest = 999
for i in range(len(S) - 2):
    X = int(S[i:i + 3])
    smallest = min(abs(X - 753), smallest)
print(smallest)
