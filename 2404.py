from typing import List
from collections import Counter


def mostFrequentEven(nums: List[int]) -> int:
    cnt = Counter()
    for num in nums:
        if num % 2 == 0:
            cnt[num] += 1
    res, resVal = -1, -1
    for key, val in cnt.items():
        if val > resVal:
            res = key
            resVal = val
        if val == resVal and key < res:
            res = key
    return res
