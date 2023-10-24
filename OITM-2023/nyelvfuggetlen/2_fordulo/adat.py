import math

class DataStructure:
    def __init__(self):
        self.list = []

    def push_back(self, x):
        self.list.append(x)

    def pop_middle(self):
        if len(self.list) == 0:
            return 0
        else:
            index = math.floor(len(self.list) / 2)
            return self.list.pop(index)

def calculate_sum(filename):
    ds = DataStructure()
    sum = 0
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() == 'p':
                sum += ds.pop_middle()
            else:
                ds.push_back(int(line.strip()))
    return sum


if __name__ == "__main__":
    print(calculate_sum("OITM-2023/nyelvfuggetlen/adat3.in.txt"))
