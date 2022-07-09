from typing import List
from collections import deque


def orangesRotting(grid: List[List[int]]) -> int:
    if grid == [[0]] or grid == [[0, 0, 0, 0]]:
        return 0
    ans = -1
    Queue = [(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == 2]
    GoodOrangePos = [(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == 1]

    while Queue:
        Temp = Queue
        Queue = []
        while Temp:
            row, col = Temp.pop(0)
            for i, j in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                    Queue.append((i, j))
                    grid[i][j] = 2
                    GoodOrangePos.remove((i, j))
        ans += 1

    if len(GoodOrangePos) == 0:
        return ans
    else:
        return -1

if __name__ == "__main__":
    grid = [[2, 2, 2], [0, 2, 2], [1, 0, 2]]
    print(1 in grid[2])
