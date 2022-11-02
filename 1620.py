import math
from typing import List


def bestCoordinate(towers: List[List[int]], radius: int) -> List[int]:
    xMax, yMax = max(tower[0] for tower in towers), max(tower[1] for tower in towers)
    ResX, ResY, ResQ = 0, 0, 0
    for x in range(xMax + 1):
        for y in range(yMax + 1):
            Quality = 0
            for nx, ny, val in towers:
                d = math.sqrt((nx - x) ** 2 + (ny - y) ** 2)
                if d <= radius:
                    Quality += int(val / (1 + d))
            if Quality > ResQ:
                ResX = x
                ResY = y
                ResQ = Quality
            if Quality == ResQ:
                if ResX > x:
                    ResX = x, ResY = y
                if ResX == x and ResY > y:
                    ResX = x, ResY = y
    return [ResX, ResY]
