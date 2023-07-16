from typing import List


def sumOfDistancesInTree(n: int, edges: List[List[int]]) -> List[int]:
    maps = [[] for _ in range(n)]
    for x, y in edges:
        maps[x].append(y)
        maps[y].append(x)

    ans = [0] * n
    size = [1] * n

    def DFS(x, fa, depth):
        ans[0] += depth
        for node in maps[x]:
            if node != fa:
                DFS(node, x, depth + 1)
                size[x] += size[node]

    DFS(0, -1, 0)

    def Reroot(x, fa):
        for node in maps[x]:
            if node != fa:
                ans[node] += ans[x] + n - 2 * size[node]
                Reroot(node, x)

    Reroot(0, -1)
    return ans
