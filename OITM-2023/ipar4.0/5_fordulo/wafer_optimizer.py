import os


def load_data(file_name: str) -> (int, int, list[int]):
    with open(os.path.join(os.getcwd(), file_name), "r") as f:
        n, k = (int(x) for x in f.readline().strip().split())
        wafers = [int(number) for number in f.readline().strip().split()]
        return n, k, wafers


def find_longest_subsequence(wafers: list[int], k) -> list[int]:
    """Find the longest subsequence of wafers where:
    the elements of the subsequence are at most k difference to each other.
    
    Args:
        wafers (list[int]): The list of wafers.
        k (int): The maximum difference between the elements of the subsequence.
    
    Returns:
        list[int]: The longest subsequence satisfying the rule.
    """
    longest_subsequence = []
    current_subsequence = []
    for i in range(len(wafers)):
        if len(current_subsequence) == 0:
            current_subsequence.append(wafers[i])
        elif abs(wafers[i] - max(current_subsequence)) <= k and abs(wafers[i] - min(current_subsequence)) <= k:
            current_subsequence.append(wafers[i])
        else:
            if len(current_subsequence) > len(longest_subsequence):
                longest_subsequence = current_subsequence
            current_subsequence = [wafers[i]]
    if len(current_subsequence) > len(longest_subsequence):
        longest_subsequence = current_subsequence
    return longest_subsequence
    

if __name__ == "__main__":
    for filename in os.listdir(os.path.join(os.getcwd())):
        if filename.endswith(".txt") and (filename.startswith("teszt_input") or filename.startswith("input")):
            n, k, wafers = load_data(filename)
            print(f"{filename}: Max subsequence with {k} max diff = {len(find_longest_subsequence(wafers, k))}")
