from math import inf
from typing import List


def minFallingPathSum(grid: List[List[int]]) -> int:
    n = len(grid)
    d = [[10 ** 9 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        d[0][i] = grid[0][i]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if j == k:
                    continue
                d[i][j] = min(d[i][j], d[i - 1][k] + grid[i][j])
    return min(d[n - 1])
