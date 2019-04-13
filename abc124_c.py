S = input()
S1 = S[0::2]
S2 = S[1::2]

S1white = S1.count("1")  # 黒にしなければいけない個数
S2white = S2.count("1")

print(min(S1white + len(S2) - S2white, len(S1) - S1white + S2white))
