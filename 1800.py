from typing import List
from math import inf


def maxAscendingSum(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    Max = -inf
    Index = 1
    while Index < len(nums):
        Temp = 0
        while Index < len(nums) and nums[Index - 1] < nums[Index]:
            Temp += nums[Index - 1]
            Index += 1
        Temp += nums[Index - 1]
        Max = max(Max, Temp)
        Index += 1
    return Max
