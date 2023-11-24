import os
from multiprocessing import Pool
import numpy as np
from numba import jit, prange



def load_data(file_name: str) -> list[list[int]]:
    with open(os.path.join(os.getcwd(), file_name), "r") as f:
        t = [int(number) for number in f.readline().split()]
        return t


@jit(nopython=True, parallel=True)
def count_parcels_jit(cx, cy, a, b):
    count = 0
    for x in prange(cx - a, cx + a + 1):
        for y in prange(cy - b, cy + b + 1):
            if ((x + 0.5 - cx) / a) ** 2 + ((y + 0.5 - cy) / b) ** 2 <= 1:
                count += 1
    return count


def count_parcels(cx, cy, a, b):
    return sum(1 for x in range(cx - a, cx + a) for y in range(cy - b, cy + b)
                if ((x + 0.5 - cx) / a) ** 2 + ((y + 0.5 - cy) / b) ** 2 <= 1)



def check_parcel(args):
    x, y, cx, cy, a, b = args
    return ((x + 0.5 - cx) / a) ** 2 + ((y + 0.5 - cy) / b) ** 2 <= 1


def count_parcels_mp(cx, cy, a, b):
    with Pool() as pool:
        parcels = pool.map(check_parcel, [
            (x, y, cx, cy, a, b)
            for x in range(cx - a, cx + a + 1)
            for y in range(cy - b, cy + b + 1)
        ])
    return sum(parcels)


def count_parcels_np(cx, cy, a, b):
    x, y = np.meshgrid(
        np.arange(cx - a, cx + a + 1),
        np.arange(cy - b, cy + b + 1)
    )
    return np.sum(((x + 0.5 - cx) / a) ** 2 + ((y + 0.5 - cy) / b) ** 2 <= 1)


def count_parcels_nps(cx, cy, a, b):
    x, y = np.meshgrid(
        np.arange(cx - a, cx + a + 1, dtype=np.int32),
        np.arange(cy - b, cy + b + 1, dtype=np.int32),
        sparse=True,
        copy=False
    )
    return np.sum(((x + 0.5 - cx) / a) ** 2 + ((y + 0.5 - cy) / b) ** 2 <= 1, dtype=np.uint16)


if __name__ == "__main__":
    for filename in sorted(os.listdir(os.getcwd())):
        if filename.endswith(".in.txt") and filename.startswith("parcella"):
            cx, cy, a, b = load_data(filename)
            print(f"{filename} numpy: {count_parcels_jit(cx, cy, a, b)}")
            #print(f"{filename} numpy: {count_parcels(cx, cy, a, b)}")
            #print(f"{filename} numpy: {count_parcels_mp(cx, cy, a, b)}")
            #print(f"{filename} numpy: {count_parcels_nps(cx, cy, a, b)}")
            #print(f"{filename} iterative: {count_parcels(cx, cy, a, b)}")
