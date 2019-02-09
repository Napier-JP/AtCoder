path = {1: 0, 2: 0, 3: 0, 4: 0}
odd = 0
for _ in range(3):
    ai, bi = map(int, input().split())
    path[ai] += 1
    path[bi] += 1

for count in path.values():
    if count % 2 == 1:
        odd += 1

if odd == 2:
    print("YES")
else:
    print("NO")
