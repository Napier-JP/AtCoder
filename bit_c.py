N, D = map(int,input().split())
coord = list(map(int,input().split()))


for i in range(N):
    print("i=",i)
    print("possible k=",list(filter(lambda x: coord[i]+D < x <= coord[i]+2*D, coord)))
    kList = list(filter(lambda x: coord[i]+D < x <= coord[i]+2*D, coord))
    for k in kList:
        print("k=",k)
        print("possible j=",list(filter(lambda x: coord[i] < x <= coord[i]+D and k-D <= x, coord)))


#filter(lambda x: coord[i]+D < x <= coord[i]+2*D, coord)
