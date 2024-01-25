from typing import List


def sumIndicesWithKSetBits(nums: List[int], k: int) -> int:
    ans = 0
    for index, num in enumerate(nums):
        if bin(index).count('1') == k:
            ans = ans + num
    return ans
