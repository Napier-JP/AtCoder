import copy

A, B = map(int,input().split())
rowBlack = ['#' for i in range(100)]
rowWhite = ['.' for i in range(100)]
grid = [rowBlack for i in range(50)]
rowHalf_half_a = ['.#' for i in range(50)] #成分を50ずつ増やす行(白始まり)
rowHalf_half_b = ['#.' for i in range(50)] #成分を50ずつ増やす行(黒始まり)
swapRowForBlack = copy.deepcopy(rowWhite) #端数処理行白から黒へ
swapRowForWhite = copy.deepcopy(rowBlack) #端数処理行黒から白へ
for i in range(50):
    grid.append(rowWhite)

for o in range((A-1)//50 - (A-1)//100):
    grid[2*o] = rowHalf_half_b
for p in range((A-1)//100):
    grid[1+2*p] = rowHalf_half_a
for q in range((B-1)//50 - (B-1)//100):
    grid[99-2*q] = rowHalf_half_a
for r in range((B-1)//100):
    grid[98-2*r] = rowHalf_half_b
#端数処理
for m in range((A-1)%50):
    swapRowForWhite[2*m] = '.'
for n in range((B-1)%50):
    swapRowForBlack[2*n] = '#'
    
grid[(A-1)//50] = swapRowForWhite
grid[99-(B-1)//50] = swapRowForBlack
print('100 100')
for z in range(100):
    ans = ''.join(grid[z])
    print(ans)
