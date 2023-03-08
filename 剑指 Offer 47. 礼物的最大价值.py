from typing import List


def maxValue(grid: List[List[int]]) -> int:
    vals = [[0 for _ in grid[0]] for _ in grid]
    for index, val in enumerate(grid[0]):
        if index == 0:
            vals[0][index] = val
        else:
            vals[0][index] = val + vals[0][index - 1]

    for index in range(len(grid)):
        if index == 0:
            vals[0][index] = grid[index][0]
        else:
            vals[index][0] = grid[index][0] + vals[index - 1][0]

    for indexI in range(1, len(grid)):
        for indexJ in range(1, len(grid[0])):
            vals[indexI][indexJ] = max(vals[indexI - 1][indexJ], vals[indexI][indexJ - 1]) + grid[indexI][indexJ]
    return vals[-1][-1]
