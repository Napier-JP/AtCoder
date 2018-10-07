N, M = map(int, input().split())
pList = input().split()
pList_int = [int(s) for s in pList]
linkDict = {i+1 : set() for i in range(N)} #各ノードをキーとし、つながっているノードの集合(set)を値とするdict
uncheckedNodes = {i+1 for i in range(N)} #孤独なノードの集合(set)
graphDict = {} #リストだと遅いのでキーを通し番号、値を相互に行き来できる番号の集合(set)としたdict
count = 0

for _ in range(M):
    x, y = map(int, input().split())
    linkDict[x].add(y)
    linkDict[y].add(x)

def link_after_link(nodeNum):
    for link in linkDict[i+1]:
        if link > i+1:
            graphDict[i+1].add(link)
            return link_after_link(link)
        
for i in range(N):
    if i+1 in uncheckedNodes:
        graphDict[i+1] = {i+1}
        uncheckedNodes.remove(i+1)
        link_after_link(i+1)


            
for i in range(N):
    if i+1 == pList_int[i]:
        count += 1
    elif pList_int[i] in linkDict[i+1]:
        count += 1
print(linkDict)
print(count)
