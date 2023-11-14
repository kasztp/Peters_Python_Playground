import os


def load_data(file_name: str) -> list[(int, int)]:
    with open(os.path.join(os.getcwd(), file_name), "r") as f:
        k = int(f.readline().strip())
        roads = [road for road in (numbers.strip().split() for numbers in f.readlines())]
        return roads


def calculate_number_of_islands(roads: list[(int, int)]) -> int:
    """
    Calculate the number of components (disconnected graphs) in the given road network.

    :param roads: The roads in the network.
    :return: The number of islands.
    """
    graph = {}
    for u, v in roads:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    def dfs(node):
        stack = [node]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(graph[node])

    islands = 0
    for node in graph:
        if node not in visited:
            dfs(node)
            islands += 1

    return islands



if __name__ == "__main__":
    for filename in os.listdir(os.path.join(os.getcwd())):
        if filename.endswith(".txt") and filename.startswith("sziget"):
            print(f"{filename}: {calculate_number_of_islands(load_data(filename))}")