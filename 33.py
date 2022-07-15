from typing import List


def search(nums: List[int], target: int) -> int:
    if len(nums) == 1:
        if target == nums[0]:
            return 0
        else:
            return -1
    Left, Right = 0, len(nums) - 1
    if target >= nums[Left]:
        while Left < len(nums) and target > nums[Left]:
            Left += 1
        if Left < len(nums) and nums[Left] == target:
            return Left
        else:
            return -1
    if Right >= 0 and target <= nums[Right]:
        while Right >= 0 and target < nums[Right]:
            Right -= 1
        if Right >= 0 and nums[Right] == target:
            return Right
        else:
            return -1
    return -1
