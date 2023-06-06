from typing import List
from collections import Counter


def equalPairs(grid: List[List[int]]) -> int:
    def Arr2Str(arr: List[int]) -> str:
        chars = "["
        for x in arr:
            chars += str(x) + ","
        return chars + "]"

    cnt = Counter()
    for arr in grid:
        cnt[Arr2Str(arr)] += 1

    res = 0
    for index in range(len(grid)):
        res += cnt[Arr2Str(list(grid[index][x] for x in range(len(grid))))]

    return res
