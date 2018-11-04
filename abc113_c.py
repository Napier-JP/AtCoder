N, M = map(int, input().split())
inputDict = {}  # キーは年、値は県番号
ansDict = {}  # キーは年、値は認識番号
inputOrderList = []  # 与えられた順に年を入れる
cityCountDict = {}  # キーは県番号、値は今何個目の市か

for index in range(M):
    Pi, Yi = map(int, input().split())
    inputOrderList.append(Yi)
    inputDict[Yi] = Pi
    cityCountDict[Pi] = 1

for year, pref in sorted(inputDict.items()):
    num = cityCountDict[pref]
    ansDict[year] = "{0:06d}".format(pref) + "{0:06d}".format(num)
    cityCountDict[pref] += 1

for order in inputOrderList:
    print(ansDict[order])
