S = input()

if S.count("A") == 1 and S.count("C") == 1:
    if S[0] == "A" and 2 <= S.find("C") <= len(S)-2:
        rmS = S.replace("A", "")
        rmS = rmS.replace("C", "")
        if rmS == rmS.lower():
            print("AC")
        else:
            print("WA")
    else:
        print("WA")

else:
    print("WA")
