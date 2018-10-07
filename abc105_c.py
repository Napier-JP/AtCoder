N = int(input())

ans = []

if N == 0:
    print("0")
else:
    while N != 1:
        if N%2 == 0:
            ans.append("0")
            N = N//(-2)
        else:
            ans.append("1")
            N = (N-1)//(-2)
    else:
        ans.append("1")

print("".join(ans[::-1]))
    
