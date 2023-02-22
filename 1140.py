from typing import List
from functools import lru_cache


def stoneGameII(piles: List[int]) -> int:
    n = len(piles)
    for index in range(n - 2, -1, -1):
        piles[index] += piles[index + 1]

    @lru_cache(None)
    def DFS(index=0, m=1):
        if index + 2 * m >= n:
            return piles[index]
        return piles[index] - min(DFS(index + x, max(x, m)) for x in range(1, 2 * m + 1))

    return DFS()
