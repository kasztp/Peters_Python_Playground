from collections import Counter

test_cases_task_1 = [
    [1, 2, 2, 3, 4, 1, 4, 1, 1, 2, 2, 2, 2],
    [1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2],
    [6, 8, 7, 4, 7, 3, 4, 6, 3, 6, 12, 12, 8, 4, 8, 6, 7, 12, 12, 7, 6, 8, 3,
    12, 3, 4, 4, 12, 12, 6, 7, 7, 3, 8, 6, 7, 4, 12, 8, 7, 3, 12, 12, 12, 12,
    3, 7, 12, 4, 6, 12, 8, 7, 8, 3, 8, 7, 8, 6, 7, 6, 12, 6, 6, 3, 12, 3, 6,
    6, 6, 4, 8, 6, 12, 12, 12, 7, 6, 8, 6, 4, 7, 4, 6, 8, 7, 4, 7, 3, 8, 7, 4,
    8, 8, 7, 8, 12], # sample test case
    [10, 10, 11, 10, 7, 7, 5, 7, 10, 11, 11, 7],
    [10, 8, 5, 8, 5, 5, 10, 5, 8, 10, 10, 8, 7, 6, 6],
    [11, 1, 3, 1, 2, 11, 5, 1, 2, 3, 1, 2, 3],
    [17, 19, 22, 19, 19, 22, 1,  17, 1,  12, 26, 26, 27, 12, 27, 12,
     12, 1,  17, 19, 27, 1,  12, 17, 12, 22, 17, 27, 1,  1,  26],
    [29, 28, 27, 28, 4,  28, 28, 27, 15, 19, 29, 29, 9, 19, 36, 27, 29, 28, 4,
     15, 4,  28, 28, 36, 19, 4,  15, 28, 36, 4,  4,  9, 9,  9,  27, 15, 4],
    [16, 12, 15, 13, 2, 15, 14, 4, 17, 12, 2, 16, 4, 15, 17, 12, 17, 12],
    [18, 4, 8, 18, 4,  32, 5,  21, 32, 21, 28, 4, 5,  28, 28, 21, 28, 28,
     5,  4, 8, 28, 28, 32, 18, 4,  21, 8,  4,  7, 18, 21, 18, 5,  18],
    [29, 33, 9,  25, 22, 22, 20, 45, 45, 8,  22, 23, 22, 23, 6,  23,
     8,  8,  36, 22, 22, 33, 33, 9,  45, 9,  23, 8,  23, 36, 20, 6,
     25, 36, 6,  33, 9,  33, 8,  33, 36, 22, 22, 25, 8,  22, 29, 9],
    [82, 9,  15, 82, 57, 9,  76, 90, 82, 45, 1,  76, 90, 90, 76, 64, 15, 90, 16,
     16, 29, 45, 90, 82, 16, 45, 45, 76, 16, 76, 27, 15, 27, 29, 16, 1,  1,  76,
     15, 90, 90, 90, 76, 9,  82, 16, 90, 15, 27, 45, 64, 9,  1,  1,  82, 90, 57,
     45, 27, 57, 29, 16, 57, 90, 1,  45, 82, 82, 9,  82, 57, 64, 16, 9,  64, 57,
     29, 45, 29, 29, 82, 82, 1,  15, 45, 29, 82, 82, 64, 9,  1],
    [58,  140, 109, 92,  106, 86,  86,  93,  59,  22,  35,  10,  10, 59,  58,
     8,   92,  8,   86,  86,  53,  8,   35,  92,  92,  22,  140, 22, 22,  109,
     140, 106, 106, 53,  106, 35,  58,  140, 35,  93,  93,  58,  59, 10,  109,
     53,  59,  10,  59,  109, 59,  106, 140, 58,  10,  22,  86,  92, 92,  10,
     10,  59,  59,  109, 140, 8,   35,  106, 93,  53,  86,  10,  86, 140, 106,
     58,  35,  109, 58,  35,  22,  35,  8,   35,  22,  22,  22,  10, 93,  92,
     106, 93,  8,   53,  86,  106, 8,   93,  93,  92,  140, 35,  10, 109, 53,
     59,  53,  58,  22,  22,  22,  8,   92,  58,  106, 92,  22,  8,  140, 59,
     10,  109, 22,  22,  35,  53,  58,  53,  53,  35,  10,  93,  93, 22,  22,
     59,  10,  86,  140, 35,  140, 92,  92,  140, 58,  140, 106]
]

test_cases_task_2 = [
    [1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2],
    [6, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 6, 6, 5, 5, 6, 6, 6],
    [4, 4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 4, 4, 4, 3, 3, 4, 3, 4, 4, 3, 3,
     4, 4, 3, 3, 3], # sample test case
    [4, 5, 5, 5, 4, 4, 4, 5, 4, 5],
    [10, 21, 21, 21, 10, 10, 10, 10, 10, 10, 10, 10, 21, 10, 21,
     21, 21, 10, 21, 10, 21, 21, 10, 10, 21, 10, 10, 21, 10, 10],
    [11, 11, 12, 12, 12, 11, 11, 12, 12, 11, 12, 12,
     12, 12, 11, 12, 11, 12, 11, 11, 12, 12, 12],
    [19, 5,  5,  19, 19, 19, 19, 19, 19, 19, 19, 5, 19, 19, 19,
     5,  19, 19, 19, 19, 19, 5,  5,  19, 19, 19, 5, 5,  19],
    [16, 16, 16, 6,  16, 6,  6,  16, 16, 6, 6,  6, 16, 16, 6, 16, 16, 16, 6,
     6,  16, 16, 16, 6,  16, 16, 6,  6,  6, 16, 6, 6,  16, 6, 6,  6,  6],
    [27, 27, 2, 2,  2,  2,  27, 2, 27, 27, 27, 2,  27, 2, 2, 2, 27, 2,
     2,  2,  2, 27, 27, 27, 27, 2, 27, 2,  27, 27, 27, 2, 2, 2, 2],
    [46, 46, 48, 46, 46, 48, 46, 46, 46, 48, 48, 46, 46, 46, 48, 46, 48,
     46, 46, 48, 48, 46, 48, 48, 46, 46, 46, 48, 48, 48, 48, 48, 48, 48,
     48, 46, 48, 46, 46, 48, 46, 48, 48, 46, 46, 46, 48, 46, 48, 46, 46],
    [42, 42, 42, 42, 42, 42, 10, 10, 42, 42, 42, 42, 10, 42, 10, 10, 10, 42,
     10, 10, 10, 42, 10, 42, 10, 10, 42, 10, 42, 10, 10, 42, 42, 10, 10, 42,
     10, 42, 10, 10, 42, 10, 10, 42, 42, 10, 42, 10, 42, 42, 42, 42, 10, 42,
     10, 42, 10, 10, 10, 10, 10, 42, 10, 10, 42, 42, 42, 10, 10, 42, 10, 10,
     42, 10, 42, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [51, 51, 51, 51, 49, 49, 51, 49, 49, 51, 51, 51, 51, 49, 49, 49, 49, 49, 51,
     51, 49, 49, 49, 49, 49, 49, 51, 51, 51, 51, 49, 51, 51, 51, 51, 51, 49, 49,
     49, 51, 51, 49, 49, 51, 51, 49, 51, 51, 51, 51, 49, 51, 51, 49, 49, 49, 49,
     49, 49, 51, 49, 51, 49, 51, 51, 49, 51, 49, 51, 51, 49, 51, 49, 49, 49, 49,
     51, 51, 49, 49, 49, 51, 49, 49, 49, 51, 49, 49, 51, 51, 51, 51, 51, 49, 49,
     49, 51, 51, 51, 49, 51, 49, 51, 49, 49, 51, 49, 49, 49, 49, 51, 49, 49, 51,
     49, 49, 51, 51, 49, 51, 51, 49, 51, 49, 49, 51, 51, 49, 51, 49, 51, 49, 51,
     51, 51, 51, 49, 51, 49, 51, 49, 51, 49, 49, 49, 51, 49, 51, 51, 51, 49, 51,
     49, 51, 49, 49, 49, 51, 49, 51, 49, 49, 49, 49, 49],
    [243, 243, 220, 220, 243, 220, 243, 220, 220, 220, 220, 220, 243, 243, 220,
     243, 220, 243, 220, 220, 243, 243, 243, 220, 243, 243, 220, 220, 220, 243,
     220, 220, 243, 243, 220, 220, 243, 220, 220, 220, 243, 220, 220, 243, 220,
     243, 220, 243, 220, 220, 243, 243, 220, 220, 243, 243, 220, 220, 220, 220,
     220, 243, 243, 220, 243, 220, 220, 220, 220, 220, 220, 243, 220, 243, 220,
     220, 243, 220, 220, 220, 243, 220, 243, 243, 243, 243, 220, 220, 243, 243,
     243, 220, 220, 220, 243, 243, 220, 220, 243, 220, 243, 243, 220, 220, 220,
     243, 243, 243, 243, 243, 243, 220, 220, 243, 220, 243, 220, 243, 220, 243,
     220, 220, 220, 243, 220, 220, 220, 220, 220, 243, 243, 243, 220, 220, 220,
     220, 220, 243, 243, 220, 243, 243, 243, 220, 243, 243, 243, 243, 220, 220,
     220, 220, 220, 243, 243, 243, 243, 220, 243, 243, 220, 243, 243, 243, 220,
     220, 220, 220, 220, 243, 243, 220, 220, 220, 220, 243, 243, 220, 243, 220,
     220, 243, 243, 220, 220, 220, 243, 220, 220, 243, 220, 220, 243, 243, 243,
     220, 220, 220, 220, 220, 220, 243, 220, 243, 243, 243, 243, 220, 220, 220,
     243, 220, 243, 243, 243, 243, 220, 243, 243, 220, 220, 243, 220, 243, 220,
     220, 220, 220, 243, 243, 243, 243, 220, 220, 243, 243, 243, 220, 220, 243,
     243, 243, 243, 220, 243, 220, 220, 243, 243, 220, 243, 243, 243, 220, 220,
     243, 243, 243, 243, 243, 243, 243, 243, 220, 220, 220, 243, 220, 243, 243,
     243, 220, 220, 220, 243, 220, 243, 220, 243, 220, 243, 220, 243, 220, 220,
     220, 243, 220, 220, 243, 220, 243, 243, 220, 243, 220, 220, 220, 243, 243,
     220, 243, 220, 220, 220, 220, 243, 243]]


def task_1(list_of_colors):
    """Returns the minimum amount of colors needed to repaint to make the fence a palindrome.

    :param list_of_colors: list of colors
    :return: the number of colors needed to repaint
    """
    l = len(list_of_colors)
    result = 0
    
    a_side = list_of_colors
    b_side = list(reversed(list_of_colors))

    if a_side == b_side:
        return 0
    
    for i in range(l):
        if a_side[i] != b_side[i]:
            result += 1
    
    return result // 2


def task_2(list_of_colors):
    """Returns the minimum amount of colors needed to replave with blank to make the fence a palindrome.

    :param list_of_colors: list of colors
    :return: the number of colors needed to replace with blank
    """
    l = len(list_of_colors)
    color_counts = {}
    for color in list_of_colors:
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    max_color_count = max(color_counts.values())
    return l - max_color_count
    

if __name__ == "__main__":
    results = []
    print(f"Results for task 1:")
    for i in range(len(test_cases_task_1)):
        result = task_1(test_cases_task_1[i])
        results.append(result)
        print(f"Test case {i}: {result}")
    print(f"Results to copy: {' '.join([str(a) for a in results[3:]])}")

    print(f"Results for task 2:")
    for i in range(len(test_cases_task_2)):
        print(f"Test case {i}: {task_2(test_cases_task_2[i])}")
    
    print("Results for task 3")
    for i in range(len(test_cases_task_2)):
        print(f"Test case {i + 1}: {task_2(test_cases_task_2[i])}")


        