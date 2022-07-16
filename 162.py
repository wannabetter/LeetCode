from typing import List
import math


def findPeakElement(nums: List[int]) -> int:
    def Get(Index):
        if Index == -1 or Index == len(nums):
            return -math.inf
        else:
            return nums[Index]

    Left, Right = 0, len(nums) - 1
    while Left <= Right:
        Mid = (Left + Right) // 2
        if Get(Mid - 1) < Get(Mid) > Get(Mid + 1):
            return Mid
        if Get(Mid) < Get(Mid + 1):
            Left = Mid + 1
        else:
            Right = Mid - 1
    return -1
