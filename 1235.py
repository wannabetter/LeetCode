from typing import List
from bisect import bisect_right
from math import inf


# 这个题还是不是特别懂，明天再仔细研究一下
def jobScheduling(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    jobs = sorted(zip(endTime, startTime, profit))
    f = [0] * (len(jobs) + 1)
    for i, (_, st, p) in enumerate(jobs):
        j = bisect_right(jobs, (st, inf), hi=i)
        f[i + 1] = max(f[i], f[j] + p)
    return f[-1]
