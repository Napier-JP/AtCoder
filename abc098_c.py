N = int(input())
S = input()

ans = N

if S.count("W")>0:
    Wbegin = S.index("W")

if S.count("E")>0:
    Ebegin = S[::-1].index("E")


for i in range(max(0,Wbegin-1), N-max(1, Ebegin)+1):
    ans = min(S[0:i].count("W")+S[i+1:].count("E"), ans)
print(ans)
