N,M,A,B = map(int,input().split())

Amikan = set()
for _ in range(M):
    newL, newR = map(int,input().split())
    for i in range(newL, newR+1):
        Amikan.add(i)

print(len(Amikan)*A+(N-len(Amikan))*B)

