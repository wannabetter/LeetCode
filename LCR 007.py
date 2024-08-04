from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        nums = sorted(nums)
        for first, val1 in enumerate(nums):
            if first > 0 and nums[first] == nums[first - 1]: continue
            third, target = len(nums) - 1, -nums[first]
            for second in range(first + 1, len(nums)):
                if second > first + 1 and nums[second] == nums[second - 1]: continue
                while second < third and nums[second] + nums[third] > target: third = third - 1
                if second == third: break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans