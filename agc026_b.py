T = int(input())

for _ in range(T):
    A,B,C,D = map(int,input().split())

    if A < B or B > D:
        print("No") #そもそも買えないか、毎日補充したとしてもやがて足りなくなる
    else:
        if A%B > C: 
            print("No") #いつか、「補充基準以上だが買う数よりは少ない」状況となる
        else:
            if D%B == 0:
                print("Yes") #補充される前後で在庫の剰余は変わらないのでsustainable
            else:
                if A%B + (D%B)* (-(-(C-(A%B))//(D%B))) == C: #D%BずつA%Bに足していって、Cと等しくなってしまうとそこで止まってしまうからもう一回足す
                    if A%B + (D%B)* ((-(-(C-(A%B))//(D%B)))+1) >= B:
                        print("Yes")
                    else:
                        print("No")
                else:
                    if A%B + (D%B)* (-(-(C-(A%B))//(D%B))) >= B:
                        print("Yes")
                    else:
                        print("No")
