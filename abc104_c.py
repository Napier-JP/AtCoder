D, G = map(int,input().split())

#100点、200点を1点、2点としていく

minSolve = [1000 for _ in range(G+1)] #どんなに多くても1000問解けば最高点
minSolve[0] = 0 #0点とるのには自明に0問

p = [0] #i点の問題数
c = [0] #i点問題のコンプリートボーナス

for _ in range(D):
    pi, ci = map(int,input().split())
    p.append(pi)
    c.append(ci//100)　#100で割っておく


#方針としてはvalue i weight 1のものが各pi個、value i*pi+ci weight piのものが各1個ある状態での
#0/1 knapsack問題なのではないかと考えるが実装力がなくABCとは別のタスクもあるので断念
