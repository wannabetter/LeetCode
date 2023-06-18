from typing import List
from collections import deque


def closedIsland(grid: List[List[int]]) -> int:
    ans = 0
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                grid[i][j] = 1
                queue = deque([i, j])
                close = True

                while queue:
                    x, y = queue.popleft()
                    if x == 0 or y == 0 or x == n - 1 or y == m - 1:
                        close = False
                    for offset_x, offset_y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        if 0 <= offset_x + x < n and 0 <= offset_y + y < m and grid[offset_x + x][offset_y + y] == 0:
                            grid[offset_x + x][offset_y + y] = 1
                            queue.append((offset_x + x, offset_y + y))

                if close:
                    ans += 1
    return ans
