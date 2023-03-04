from typing import List
from collections import Counter


def countTriplets(nums: List[int]) -> int:
    res = 0
    cnt = Counter(x & y for x in nums for y in nums)

    for z in nums:
        for mask, freq in cnt.items():
            if z & mask == 0:
                res += freq

    return res
