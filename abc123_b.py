import math
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
raws = [A, B, C, D, E]
residues = []
for num in raws:
    if num % 10 != 0:
        residues.append(num % 10)
    else:
        residues.append(10)

ans = 0
lastDish = residues.index(min(residues))
for i in range(len(raws)):
    if i != lastDish:
        ans += math.ceil(raws[i] / 10) * 10
    else:
        ans += raws[i]
print(ans)
