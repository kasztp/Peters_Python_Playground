import os

def load_data(filename: str) -> str:
    with open(os.path.join(os.getcwd(), filename), "r") as f:
        return f.readline().strip()


def longest_boring_substring(word):
    n = len(word)
    longest = 0
    for length in range(1, n//2+1):
        for i in range(n - 2*length + 1):
            if word[i:i+length] == word[i+length:i+2*length]:
                longest = max(longest, 2*length)
    return longest


print(longest_boring_substring('pompom'))  # 6
print(longest_boring_substring('madareteto'))  # 4
print(longest_boring_substring('tettetett'))  # 6
print(longest_boring_substring('burgonya'))  # 0
print(longest_boring_substring('babbbabababaaab'))  # 8
print(longest_boring_substring('bcbaabacaccaacccccbccccbcbabccbcbabacabcbabbacacaa'))  # 14


if __name__ == "__main__":
    for i in range(1, 6):
        filename = f"unalmas{i}.in.txt"
        print(f'{filename}: {longest_boring_substring(load_data(filename))}')
