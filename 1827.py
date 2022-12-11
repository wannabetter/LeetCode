from typing import List


def minOperations(nums: List[int]) -> int:
    Index, Res = 1, 0
    while Index < len(nums):
        if nums[Index - 1] >= nums[Index]:
            Res += nums[Index - 1] - nums[Index] + 1
            nums[Index] += nums[Index - 1] - nums[Index] + 1
        Index += 1
    return Res
