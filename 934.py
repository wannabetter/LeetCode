from math import inf
from typing import List


def shortestBridge(grid: List[List[int]]) -> int:
    for IndexI, Row in enumerate(grid):
        for IndexJ, Val in enumerate(Row):
            if Val != 1:
                continue
            isLand = []
            grid[IndexI][IndexJ] = -1
            Queue = [[IndexI, IndexJ]]
            while Queue:
                X, Y = Queue.pop(0)
                isLand.append([X, Y])
                for OffsetX, OffsetY in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    if 0 <= X + OffsetX < len(grid[0]) and 0 <= Y + OffsetY < len(grid) and grid[X + OffsetX][
                        Y + OffsetY] == 1:
                        grid[X + OffsetX][Y + OffsetY] = -1
                        Queue.append([X + OffsetX, Y + OffsetY])

            Step = 0
            Queue = isLand
            while Queue:
                Temps = Queue
                Queue = []
                for X, Y in Temps:
                    for OffsetX, OffsetY in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                        if 0 <= X + OffsetX < len(grid[0]) and 0 <= Y + OffsetY < len(grid):
                            if grid[X + OffsetX][Y + OffsetY] == 1:
                                return Step
                            if grid[X + OffsetX][Y + OffsetY] == 0:
                                grid[X + OffsetX][Y + OffsetY] = -1
                                Queue.append([X + OffsetX, Y + OffsetY])
                Step += 1
