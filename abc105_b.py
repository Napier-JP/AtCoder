N = int(input())

if N <= 3 or 5<= N <= 6:
    print("No")
else:
    while True:
        if N < 0:
            print("No")
            break
        elif N%4 == 0:
            print("Yes")
            break
        N = N-7


