N = int(input())

count = 0

while N > 5:
    six_jousu = 1
    nine_jousu = 1
    
    while N >= 6**six_jousu:
        six_jousu += 1
        
    print(6**(six_jousu-1), "が最大")
    
    while N >= 9**nine_jousu:
        nine_jousu += 1
    print(9**(nine_jousu-1), "が最大")
    
    N = N-max(6**(six_jousu-1), 9**(nine_jousu-1))
    print("引く数", max(6**(six_jousu-1), 9**(nine_jousu-1)))
    print("N = ", N)
    count += 1
    print("カウント",count)
count = count + N
print(count)
