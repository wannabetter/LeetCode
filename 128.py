from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 1
        seen = set(nums)

        for num in seen:
            if num - 1 not in seen:
                cur = 1
                cNum = num

                while cNum + 1 in seen:
                    cur += 1
                    cNum = cNum + 1

                ans = max(ans, cur)

        return ans