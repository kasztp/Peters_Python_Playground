# TODO: implement solution for windows across days.
import os
import time
from collections import deque


def load_data(file_name: str) -> (int, int, int, list[int]):
    with open(os.path.join(os.getcwd(), file_name), "r") as f:
        lines = f.readlines()
        n, k = (int(i) for i in lines[0].split())
        times = [[int(x) for x in time_str.strip().split()] for time_str in lines[1:]]
        time_secods = [time[0] * 3600 + time[1] * 60 + time[2] for time in times]
        return n, k, sorted(time_secods)


def get_max_num_violations(times: list[int], k: int) -> int:
    """
    Given the violation times in seconds, return the maximum number of possible violations of the speed limit,
    in the busiest k seconds interval window.

    params:
        times: list of timestamps in seconds
        k: number of seconds in the interval
    
    return:
        maximum number of violations
    """
    max_violations = 0
    min_window = min(times)
    max_window = max(times)

    for i in range(min_window, max_window):
        violations = len(list(filter(lambda x: i <= x < i + k, times)))
        max_violations = max(max_violations, violations)
    return max_violations


def get_max_num_violations_sliding_window(times: list[int], k: int) -> int:
    """
    Given the violation times in seconds, return the maximum number of possible violations of the speed limit,
    in the busiest k seconds interval window.

    params:
        times: list of timestamps in seconds
        k: number of seconds in the interval
    
    return:
        maximum number of violations
    """
    violations = deque()
    max_violations = 0

    for time in times:
        while violations and violations[0] < time - k:
            violations.popleft()
        violations.append(time)
        max_violations = max(max_violations, len(violations))

    return max_violations


if __name__ == "__main__":
    for i in range(2):
        filename = f"traffipax.pelda{i + 1}.in.txt"
        n, k, times = load_data(filename)
        tic = time.perf_counter()
        print(f"{filename} (SW): {get_max_num_violations_sliding_window(times, k)}")
        toc = time.perf_counter()
        print(f"Time for Sliding Window run: {toc - tic:0.4f} seconds")
        tic = time.perf_counter()
        print(f"{filename} (S): {get_max_num_violations(times, k)}")
        toc = time.perf_counter()
        print(f"Time for Sequential run: {toc - tic:0.4f} seconds")
