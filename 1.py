from typing import List
from collections import Counter


def twoSum(nums: List[int], target: int) -> List[int]:
    cnt = Counter()
    for index, num in enumerate(nums):
        if target - num in cnt:
            return [cnt[target - num], index]
        else:
            cnt[num] = index
