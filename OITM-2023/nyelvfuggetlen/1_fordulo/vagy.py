import numpy as np


numbers = [1,7,1000,10021300,10000000000,138312987492713,9823479283741249862340130780373338801]


def vagyolo(x: int) -> int:
    result = 1
    for i in range(x + 1):
        result = result | i
    return result

def np_vagyolo(x: int) -> int:
    arr = np.arange(x+1)
    return np.bitwise_or.reduce(arr, axis=0)


def tricky_vagyolo(x: int) -> int:
    return 2**(x.bit_length()) - 1


for number in numbers:
    print(f"IN: {number}, OUT: {tricky_vagyolo(number)}")
