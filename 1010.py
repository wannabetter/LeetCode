from typing import List
from collections import Counter


def numPairsDivisibleBy60(time: List[int]) -> int:
    res = 0
    cnt = Counter()
    for t in time:
        res += cnt[(60 - t % 60) % 60]
        cnt[t % 60] += 1
    return res
