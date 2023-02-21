from typing import List


def minTaps(n: int, ranges: List[int]) -> int:
    rightMost = [0] * (n + 1)
    for i, r in enumerate(ranges):
        left = max(i - r, 0)
        rightMost[left] = max(rightMost[left], i + r)

    res = 0
    nextPos = 0
    curPos = 0
    for i in range(n):
        nextPos = max(nextPos, rightMost[i])
        if i == curPos:
            if i == nextPos:
                return -1
            curPos = nextPos
            res += 1
    return res