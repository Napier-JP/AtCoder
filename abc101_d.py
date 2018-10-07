K = int(input())

for i in range(1,K+1): #1からKまで
    ansStr = ""
    ansStr += "9"*(i//9)
    if i%9 == 0:
        print(ansStr)
    else:
        print(str(i%9)+ansStr)
    
