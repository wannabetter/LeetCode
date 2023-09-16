from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) <= 2:
        return max(nums)
    dp = [nums[0], max(nums[0], nums[1])]
    for index in range(2, len(nums)):
        dp.append(max(dp[-1], dp[-2] + nums[index]))
    return dp[-1]