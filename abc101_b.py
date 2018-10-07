N = input()

intN = int(N)
count = 0

for digit in N:
    count += int(digit)

print("Yes" if intN%count == 0 else "No")
