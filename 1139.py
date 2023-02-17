from typing import List
from itertools import accumulate


def largest1BorderedSquare(grid: List[List[int]]) -> int:
    row, col = len(grid), len(grid[0])

    rowArr = [list(accumulate(row, initial=0)) for row in grid]
    colArr = [list(accumulate(col, initial=0)) for col in zip(*grid)]

    for dist in range(min(row, col), 0, -1):
        for i in range(row - dist + 1):
            for j in range(col - dist + 1):
                if rowArr[i][j + dist] - rowArr[i][j] == dist and rowArr[i + dist - 1][j + dist] - rowArr[i + dist - 1][
                    j] == dist and colArr[j][i + dist] - colArr[j][i] == dist and colArr[j + dist - 1][i + dist] - \
                        colArr[j + dist - 1][i] == dist:
                    return dist * dist
    return 0
