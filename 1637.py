from typing import List


def maxWidthOfVerticalArea(points: List[List[int]]) -> int:
    points = sorted(points, key=lambda x: x[0])
    res = 0
    for index in range(1, len(points)):
        res = max(res, points[index][0] - points[index-1][0])
    return res
