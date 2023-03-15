from typing import List


def maximalNetworkRank(n: int, roads: List[List[int]]) -> int:
    maps = [[] for _ in range(n)]

    for node1, node2 in roads:
        maps[node1].append(node2)
        maps[node2].append(node1)

    res = -1

    for node1 in range(n):
        temp = len(maps[node1])
        for node2 in range(node1 + 1, n):
            x = temp + len(maps[node2])
            if node1 in maps[node2]:
                x -= 1
            res = max(res, temp + x)
    return res
