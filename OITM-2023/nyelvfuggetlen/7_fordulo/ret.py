import os

def load_data(file_name: str) -> list[list[int]]:
    with open(os.path.join(os.getcwd(), file_name), "r") as f:
        t = [[int(number) for number in numbers.strip()] for numbers in f.readlines()]
        #print(t)
        return t


def min_effort(field):
    n = len(field)
    m = len(field[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + (field[i][0] != field[i-1][0]) * i
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + (field[0][j] != field[0][j-1]) * j
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(
                dp[i-1][j] + (field[i][j] != field[i-1][j]) * (i+j),
                dp[i][j-1] + (field[i][j] != field[i][j-1]) * (i+j)
            )
    return dp[-1][-1]


if __name__ == "__main__":
    for filename in sorted(os.listdir(os.getcwd())):
        if filename.endswith(".in.txt") and filename.startswith("ret"):
            field = load_data(filename)
            print(f"{filename}: {min_effort(field)}")
