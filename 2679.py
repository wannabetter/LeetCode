from typing import List


def matrixSum(nums: List[List[int]]) -> int:
    ans = 0
    for num in nums:
        num.sort()
    for num in zip(*nums):
        ans += max(num)
    return ans
