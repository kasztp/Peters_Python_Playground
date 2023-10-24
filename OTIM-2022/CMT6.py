import sys

sys.setrecursionlimit(20000)


def concat_with(text, items=[]):
    items.append(text)
    return items

print(sum([*concat_with(1, [2]),
            *concat_with(3),
            *concat_with(4)]))

cache = {1: 1, 2: 3}


def f(x):
    if x == 1:
        return 1
    if x not in cache:
        cache[x] = x * (f(x - 1) % x) + f(x - 1)
        #print(cache)
    return cache[x]


print(f(10))
print(f(100))
print(f(10001))
