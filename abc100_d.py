N, M = map(int, input().split())

cakesPPP = []
cakesPPN = []
cakesPNP = []
cakesNPP = []
cakesPNN = []
cakesNPN = []
cakesNNP = []
cakesNNN = []

for _ in range(N):
    x, y, z = map(int, input().split())
    if x >= 0 and y >= 0 and z >= 0:
        cakesPPP.append(abs(x)+abs(y)+abs(z))
    elif x >= 0 and y >= 0 and z < 0:
        cakesPPN.append(abs(x)+abs(y)+abs(z))
    elif x >= 0 and y < 0 and z >= 0:
        cakesPNP.append(abs(x)+abs(y)+abs(z))
    elif x < 0 and y >= 0 and z >= 0:
        cakesNPP.append(abs(x)+abs(y)+abs(z))
    elif x >= 0 and y <0 and y < 0:
        cakesPNN.append(abs(x)+abs(y)+abs(z))
    elif x < 0 and y >= 0 and z < 0:
        cakesNPN.append(abs(x)+abs(y)+abs(z))
    elif x < 0 and y < 0 and z >= 0:
        cakesNNP.append(abs(x)+abs(y)+abs(z))
    else:
        cakesNNN.append(abs(x)+abs(y)+abs(z))
print(sum(sorted(cakesPPP)[0:M]), sum(sorted(cakesPPN)[0:M]), sum(sorted(cakesPNP)[0:M]), sum(sorted(cakesNPP)[0:M]), sum(sorted(cakesPNN)[0:M]), sum(sorted(cakesNPN)[0:M]), sum(sorted(cakesNNP)[0:M]), sum(sorted(cakesNNN)[0:M]))
print(max(sum(sorted(cakesPPP)[0:M]), sum(sorted(cakesPPN)[0:M]), sum(sorted(cakesPNP)[0:M]), sum(sorted(cakesNPP)[0:M]), sum(sorted(cakesPNN)[0:M]), sum(sorted(cakesNPN)[0:M]), sum(sorted(cakesNNP)[0:M]), sum(sorted(cakesNNN)[0:M])))
