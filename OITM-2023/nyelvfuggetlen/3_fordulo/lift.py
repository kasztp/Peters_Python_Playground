import os
from itertools import combinations


def load_data(file_name: str) -> (int, int, int, list[int]):
    with open(os.path.join(os.getcwd(), file_name), "r") as f:
        lines = f.readlines()
        n, k, w = (int(i) for i in lines[0].split())
        numbers = [int(student) for student in lines[1].split()]
        return n, k, w, numbers


def get_num_combinations(numbers: list[int], n: int, k: int, w: int) -> int:
    """
    Return the number of combinations where:
    the munber of elements is k,
    and the sum of the k numbers is w.
    """
    return sum(sum(combination) == w for combination in combinations(numbers, k))


def get_num_combinations_dp(numbers: list[int], n: int, k: int, w: int) -> int:
    """
    Return the number of combinations where:
    the munber of elements is k,
    and the sum of the k numbers is w.

    This function uses dynamic programming.
    """
    dp = [[[0 for _ in range(w + 1)] for _ in range(k + 1)] for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            for l in range(1, w + 1):
                dp[i][j][l] = dp[i - 1][j][l]
                if numbers[i - 1] <= l:
                    dp[i][j][l] += dp[i - 1][j - 1][l - numbers[i - 1]]
    
    return dp[n][k][w]


if __name__ == "__main__":
    for i in range(5):
        filename = f"lift{i + 1}.in.txt"
        n, k, w, numbers = load_data(filename)
        print(f"{filename}: {get_num_combinations_dp(numbers, n, k, w)}")
