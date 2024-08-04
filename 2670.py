from typing import List

def distinctDifferenceArray(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0] * n

    for index in range(n):
        ans[index] = len(set(nums[:index + 1])) - len(set(nums[index + 1:]))

    return ans

