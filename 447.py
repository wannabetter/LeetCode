from math import dist
from typing import List
from collections import defaultdict


def numberOfBoomerangs(points: List[List[int]]) -> int:
    ans = 0
    for p in points:
        cnt = defaultdict(int)
        for q in points:
            dis = dist(p, q)
            cnt[dis] += 1
        for m in cnt.values():
            ans += m * (m - 1)
    return ans
