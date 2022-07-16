from typing import List


def findMin(nums: List[int]) -> int:
    Index = len(nums) - 1
    while Index > 0 and nums[Index - 1] < nums[Index]:
        Index = Index - 1
    return min(nums[0], nums[Index])
