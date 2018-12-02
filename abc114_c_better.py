import itertools

N = int(input())

li = []

for n in range(1, 10):
    for num in itertools.product("357", repeat=n):
        if(num.count("3") and num.count("5") and num.count("7")):
            li.append(int("".join(num)))

print(len([i for i in li if i <= N]))
