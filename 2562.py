from typing import List


def findTheArrayConcVal(nums: List[int]) -> int:
    ans = 0
    left, right = 0, len(nums) - 1
    while left <= right:
        if left == right:
            ans += nums[left]
        else:
            ans += int(str(nums[left]) + str(nums[right]))
        left += 1
        right -= 1
    return ans
