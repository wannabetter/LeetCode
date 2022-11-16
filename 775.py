from typing import List


def isIdealPermutation(nums: List[int]) -> bool:
    MinSuf = nums[-1]
    for Index in range(len(nums) - 2, 0, -1):
        if nums[Index - 1] > MinSuf:
            return False
        MinSuf = min(MinSuf, nums[Index])
    return True
