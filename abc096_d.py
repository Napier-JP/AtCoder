N = int(input())
ansList = []

def Eratosthenes_div5amari1(N):
    li = [i for i in range(2, N+1)]
    serial = []
    amari1 = []
    while li:
        li.sort()
        num = li[0]
        if num % 5 == 1:
            amari1.append(num)
        serial = [k * num for k in range(1, N//num + 1)]
        li = list(set(li) - set(serial))
    return(amari1)
        
ansList = list(map(str, Eratosthenes_div5amari1(1500)))
print(" ".join(ansList[0:N]))
