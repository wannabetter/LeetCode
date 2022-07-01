from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            print(left,right)
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        nums.insert(left,target)
        return left