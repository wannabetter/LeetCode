from typing import List


def deleteGreatestValue(grid: List[List[int]]) -> int:
    for i in grid:
        i.sort()
    return sum([max(i) for i in zip(*grid)])