from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) <= 2:
        return max(nums)
    dp1 = [nums[0], max(nums[0], nums[1])]
    for index in range(2, len(nums) - 1):
        dp1.append(max(dp1[-1], dp1[index - 2] + nums[index]))
    dp2 = [nums[1], max(nums[1], nums[2])]
    for index in range(2, len(nums) - 1):
        dp2.append(max(dp2[-1], dp2[index - 2] + nums[index + 1]))
    return max(dp1[-1], dp2[-1])
