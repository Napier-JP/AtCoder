distanceSum = 0
spotCount = int(input())
spotList = input().split()
spotList = [int(i) for i in spotList]
spotList.append(0)

def calcDistance(num): # 配列num-1番のスポットから配列num番目のスポットへの距離を計算
    if num == 0: #開始地点から配列0番＝最初のスポット
        return abs(spotList[num])
    elif num == spotCount: #最後スポットから開始地点
        return abs(spotList[num-1])
    else:
        return abs(spotList[num]-spotList[num-1])

def calcSkipEffect(num): #配列num番をスキップした時の移動距離への影響を計算
    if num == 0: #最初のスポットの時だけの例外
        return abs(spotList[num+1])-abs(spotList[num])-abs(spotList[num+1]-spotList[num])
    else:
        return abs(spotList[num+1]-spotList[num-1])-abs(spotList[num]-spotList[num-1])-abs(spotList[num+1]-spotList[num])

for i in range(spotCount+1): #総移動回数はスポット数+1
    distanceSum += calcDistance(i)
    
for j in range(spotCount): #配列0～n-1番までの各スポットについて実行
    print(str(distanceSum + calcSkipEffect(j)))
