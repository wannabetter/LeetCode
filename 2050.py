from typing import List
from functools import lru_cache


def minimumTime(n: int, relations: List[List[int]], time: List[int]) -> int:
    ans = 0
    prev = [[] for _ in range(n + 1)]
    for x, y in relations:
        prev[y].append(x)

    @lru_cache(None)
    def DP(index):
        cur = 0
        for p in prev[index]:
            cur = max(cur, DP(p))
        cur += time[index - 1]
        return cur

    for index in range(1, n + 1):
        ans = max(ans, DP(index))
    return ans
