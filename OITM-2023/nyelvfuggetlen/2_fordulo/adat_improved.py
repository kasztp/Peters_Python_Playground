import collections


class DataStructure:
    def __init__(self):
        self.deque = collections.deque()

    def push_back(self, x):
        self.deque.append(x)
        return 0

    def pop_middle(self):
        if len(self.deque) == 0:
            return 0
        else:
            index = len(self.deque) // 2
            value = self.deque[index]
            del self.deque[index]
            return value


def calculate_sum(filename):
    ds = DataStructure()
    with open(filename, 'r') as file:
        lines = file.readlines()
        numbers = [ds.pop_middle() if line.strip() == 'p' else ds.push_back(int(line.strip())) for line in lines]
    return sum(numbers)


if __name__ == "__main__":
    print(calculate_sum("OITM-2023/nyelvfuggetlen/adat3.in.txt"))
