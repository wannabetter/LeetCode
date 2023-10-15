from typing import List

def singleNumber(nums: List[int]) -> int:
    return next(k for k, v in Counter(nums).items() if v == 1)