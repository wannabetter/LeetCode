import math
from typing import List


def nearestValidPoint(x: int, y: int, points: List[List[int]]) -> int:
    Res = math.inf
    ResIndex = -1
    for Index, (PointX, PointY) in enumerate(points):
        if (PointX == x or PointY == y) and (abs(PointX - x) + abs(PointY - y)) < Res:
            Res = (abs(PointX - x) + abs(PointY - y))
            ResIndex = Index
    return ResIndex
