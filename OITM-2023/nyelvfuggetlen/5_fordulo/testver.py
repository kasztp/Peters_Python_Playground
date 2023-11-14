import os
from itertools import combinations


def load_data(file_name: str) -> list[int]:
    with open(os.path.join(os.getcwd(), file_name), "r") as f:
        t = [int(number) for number in f.readline().strip().split()]
        return t


def get_n_sum_combinations(t: list[int], n: int, d: int) -> dict[tuple[int]: int]:
    print(n-d, n+d)
    len_t = len(t)
    combos = {}
    for i in range(len_t // 2 -1, len_t // 2 + len_t//4):
        combos.update({tuple(perm):sum(perm) for perm in combinations(t, i) if n-d <= sum(perm) <= 2*n})
    return combos


def pair_permutations(perm: dict[tuple[int]: int], n: int) -> tuple[int, int]:
    """Pair permutations where the sum is the closest to 2*n but not greater than 2*n,
    and the permutations in the pair don't contain the same number.

    :param perm: The permutations.
    :param n: The target sum.
    :return: The paired permutations.
    """
    paired_permutations = []
    for p1, p2 in combinations(perm.items(), 2):
        # print(p1, p2)
        if p1[1] + p2[1] <= 2*n and len(set(p1[0]).intersection(set(p2[0]))) == 0:
            paired_permutations.append((p1[1], p2[1]))
    return paired_permutations


def calculate_minimum_difference(t: list[int]) -> int:
    print(f"Sum: {sum(t)} len: {len(t)}")
    n = sum(t) // 2
    print(n)
    d = max(t)
    print(d)
    n_sum_permutations = get_n_sum_combinations(t, n, d)
    # print(n_sum_permutations)
    paired_permutations = pair_permutations(n_sum_permutations, n)
    # print(paired_permutations)
    return min([abs(sum(pair) - 2*n) for pair in paired_permutations])


def calculate_minimum_difference_improved(t: list[int]) -> int:
    total_weight = sum(t)
    dp = [0] * (total_weight + 1)
    dp[0] = 1
    sum_weights = 0

    for weight in t:
        sum_weights += weight
        for j in range(sum_weights, weight - 1, -1):
            if dp[j - weight]:
                dp[j] = 1

    for diff in range(total_weight // 2, -1, -1):
        if dp[diff]:
            return total_weight - 2 * diff


if __name__ == "__main__":
    for filename in os.listdir(os.path.join(os.getcwd())):
        if filename.endswith(".txt") and filename.startswith("testver"):
            #print(f"{filename}: {calculate_minimum_difference(load_data(filename))}")
            print(f"{filename}: {calculate_minimum_difference_improved(load_data(filename))}")