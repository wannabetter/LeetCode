from typing import List


def checkXMatrix(grid: List[List[int]]) -> bool:
    sumGrid, n = 0, len(grid)
    for index in range(0, n):
        if grid[index][index] == 0 or grid[index][n - 1 - index] == 0:
            return False
        sumGrid += grid[index][index] + grid[index][n - 1 - index]
    if n % 2 != 0:
        sumGrid -= grid[n // 2][n // 2]
    return sum(sum(row) for row in grid) - sumGrid == 0