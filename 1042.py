from typing import List


def gardenNoAdj(n: int, paths: List[List[int]]) -> List[int]:
    res = [0] * n
    maps = [[] for _ in range(n)]
    for x, y in paths:
        maps[x - 1].append(y - 1)
        maps[y - 1].append(x - 1)
    for index, nodes in enumerate(maps):
        res[index] = (set(range(1, 5)) - {res[node] for node in nodes}).pop()
        print(set(range(1, 5)) - {res[node] for node in nodes})
    return res
