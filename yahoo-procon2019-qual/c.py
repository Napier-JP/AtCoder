K, A, B = map(int, input().split())
if A + 2 >= B:  # 交換は無駄
    print(K + 1)
elif K < A + 1:  # 全部たたいても交換ができない
    print(K + 1)
else:
    print(A + ((K-A+1)//2)*(B-A) + (K-A+1) % 2)
