
"""def f(x):
    cache_f = {}
    if x < 2:
        return 1
    if x in cache_f:
        return cache_f[x]
    cache_f[x] = g(x - 1) + f(x - 2)
    return f(x - 1) + g(x + 1)
"""

def f(x):
    result = [5*(2**n) -(n+4) for n in range(x+1)]
    return result[-1]


def g(x):
    if x < 2:
        return 1
    return x + f(x - 2)


print(f"1: {f(1)}")
print(f"2: {f(2)}")
print(f"3: {f(3)}")
print(f"4: {f(4)}")
print(f"5: {f(5)}")
print(f"6: {f(6)}")
print(f"7: {f(7)}")
print(f"8: {f(8)}")
print(f"9: {f(9)}")
print(f"10: {f(10)}")
print(f"20: {f(20)}")
print(f"100: {f(100)}")
print(f"1000: {f(1000)}")
