from typing import List


def maximizeSum(nums: List[int], k: int) -> int:
    return max(nums) * k + k*(k-1)//2

