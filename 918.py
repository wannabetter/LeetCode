from typing import List
from copy import deepcopy


def maxSubarraySumCircular(nums: List[int]) -> int:
    dp1 = [nums[0]]
    dp2 = [nums[0]]
    Sum = nums[0]
    for index in range(1, len(nums)):
        Sum += nums[index]
        dp1.append(max(dp1[index - 1] + nums[index], nums[index]))
        dp2.append(min(dp2[index - 1] + nums[index], nums[index]))
    if Sum == dp2[-1]:
        return dp1[-1]
    else:
        return max(dp1[-1], Sum - dp2[-1])
