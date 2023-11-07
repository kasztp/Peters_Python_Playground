import os


def load_data(file_name: str) -> (int, int):
    with open(os.path.join(os.getcwd(), file_name), "r") as f:
        t = int(f.readline().strip())
        return t


def get_shortest_path_increasing_steps(t: int) -> int:
    """
    Start from 0, go to t in the shortest amount of steps.
    
    Absolute value of the step can be 1, 2, 3, 4, 5, 6, 7, 8, 9, 10...infinite, but in this order.
    A step can be either positive or negative.

    :param t: The target number.
    :return: The minimum number of steps necessary to reach the target.
    """
    for i in range(1, 1000000):
        if i * (i + 1) // 2 >= abs(t):
            return i


def get_shortest_path_increasing_steps_improved(t: int) -> int:
    """
    Start from 0, go to t in the shortest amount of steps.
    
    Absolute value of the step can be 1, 2, 3, 4, 5, 6, 7, 8, 9, 10...infinite, but in this order.
    A step can be either positive or negative.

    :param t: The target number.
    :return: The minimum number of steps necessary to reach the target.
    """
    t = abs(t)
    step = 1
    total = 0
    while total < t:
        total += step
        step += 1
    
    if total == t or (total - t) % 2 == 0:
        return step - 1
    elif (total + step - t) % 2 == 0:
        return step
    else:
        return step + 1


if __name__ == "__main__":
    print(f"Példa: {get_shortest_path_increasing_steps(11)}")
    print(f"Példa: {get_shortest_path_increasing_steps_improved(11)}")
    for filename in os.listdir(os.path.join(os.getcwd())):
        if filename.endswith(".txt"):
            print(f"{filename}: {get_shortest_path_increasing_steps(load_data(filename))}")
            print(f"{filename}: {get_shortest_path_increasing_steps_improved(load_data(filename))}")
