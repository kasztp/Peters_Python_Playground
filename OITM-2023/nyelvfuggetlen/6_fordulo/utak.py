import os


def load_data(file_name: str) -> tuple[int, int, list[list[int]]]:
    with open(os.path.join(os.getcwd(), file_name), "r") as f:
        n, m = map(int, f.readline().split())
        r = [[int(number) for number in numbers.split()] for numbers in f.readlines()]
        return n, m, r


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        xr = self.find(x)
        yr = self.find(y)
        if xr != yr:
            if self.rank[xr] < self.rank[yr]:
                self.parent[xr] = yr
            else:
                self.parent[yr] = xr
                if self.rank[xr] == self.rank[yr]:
                    self.rank[xr] += 1


def kruskal(n: int, edges: list[list[int]]) -> int:
    uf = UnionFind(n)
    edges.sort(key=lambda x: x[2])
    res = 0
    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            res += w
    return res


if __name__ == "__main__":
    for i in range(1,6):
        filename = f"utak{i}.in.txt"
        N, M, edges = load_data(filename)
        print(f"{filename}: {kruskal(N, edges)}")
