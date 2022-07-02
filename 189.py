from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for index in range(k):
            temp = nums.pop()
            nums.insert(0, temp)
