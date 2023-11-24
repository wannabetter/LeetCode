from typing import List


def countPairs(nums: List[int], target: int) -> int:
    ans = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            ans += 1 if nums[i] + nums[j] < target else 0
    return ans