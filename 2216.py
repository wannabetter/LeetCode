from typing import List


def minDeletion(nums: List[int]) -> int:
    n = len(nums)
    ans, check = 0, True
    for index in range(n - 1):
        if nums[index] == nums[index + 1] and check:
            ans = ans + 1
        else:
            check = not check
    if (n - ans) % 2 != 0:
        ans = ans + 1
    return ans
