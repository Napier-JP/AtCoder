D, N = map(int,input().split())

li = [(100**D)*i for i in range(200) if ((100**D)*i)%(100**(D+1)) != 0]

print(li[N-1])
