from typing import List


def alternatingSubarray(nums: List[int]) -> int:
    res = -1
    n = len(nums)
    for firstIndex in range(n):
        for i in range(firstIndex + 1, n):
            length = i - firstIndex + 1
            if nums[i] - nums[firstIndex] == (length - 1) % 2:
                res = max(res, length)
            else:
                break
    return res

        