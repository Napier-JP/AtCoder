S = input()
first = int(S[0:2])
second = int(S[2:])

if 1 <= first <= 12:
    # MMYY?
    if 1 <= second <= 12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    # YYMM?
    if 1 <= second <= 12:
        print("YYMM")
    else:
        print("NA")
