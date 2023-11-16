from typing import List


def longestAlternatingSubarray(nums: List[int], threshold: int) -> int:
    ans, index = 0, 0
    while index < len(nums):
        if nums[index] % 2 == 0:
            token = 0
            while index + 1 < len(nums) and nums[index] % 2 != nums[index + 1] % 2 and nums[index] <= threshold:
                token = token + 1
                index = index + 1
            if index < len(nums) and nums[index] <= threshold:
                token = token + 1
            ans = max(ans, token)
            index = index + 1
        else:
            index = index + 1
    return ans
