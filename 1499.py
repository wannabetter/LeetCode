from math import inf
from typing import List
from collections import deque


def findMaxValueOfEquation(points: List[List[int]], k: int) -> int:
    ans = -inf
    q = deque()
    for x, y in points:
        while q and q[0][0] < x - k:
            q.popleft()
        if q:
            ans = max(ans, x + y + q[0][1])
        while q and q[-1][1] <= y - x:
            q.pop()
        q.append((x, y - x))
    return ans