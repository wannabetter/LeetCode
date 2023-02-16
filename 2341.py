from typing import List
from collections import Counter


def numberOfPairs(nums: List[int]) -> List[int]:
    res1, res2 = 0, 0
    cnt = Counter(nums)
    for val in cnt.values():
        res1 += val // 2
        res2 += val % 2
    return [res1, res2]
