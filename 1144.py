from typing import List


def movesToMakeZigzag(nums: List[int]) -> int:
    res1, res2 = 0, 0
    for index in range(len(nums)):
        if index % 2 == 0:
            dist1 = nums[index] - nums[index - 1] + 1 if index > 0 and nums[index] >= nums[index - 1] else 0
            dist2 = nums[index] - nums[index + 1] + 1 if index < len(nums) - 1 and nums[index] >= nums[index + 1] else 0
            res1 += max(dist1, dist2)
        else:
            dist1 = nums[index] - nums[index - 1] + 1 if nums[index] >= nums[index - 1] else 0
            dist2 = nums[index] - nums[index + 1] + 1 if index < len(nums) - 1 and nums[index] >= nums[index + 1] else 0
            res2 += max(dist1, dist2)
    return min(res1, res2)
