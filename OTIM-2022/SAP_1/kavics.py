import os

n , k = 0, 0
stones = []

with open(os.getcwd() + "/OTIM-2022/SAP_1/" + "kavics.pelda1.in.txt", "r", encoding="utf8") as f:
    contents = f.readlines()
    n, k = [int(x) for x in contents[0].split()]
    stones = [int(x) for x in contents[1].split()]

print(n, k)
print(stones)
maxes = sorted(stones, reverse=True)[:k]
print(maxes)
for idx, n in enumerate(maxes):
    print(f"{n} --> {stones.index(n)}")

