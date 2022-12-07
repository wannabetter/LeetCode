import math
from typing import List
from collections import Counter


def minOperations(nums1: List[int], nums2: List[int]) -> int:
    if 6 * len(nums1) > len(nums2) or 6 * len(nums2) > len(nums1):
        return -1
    Diff = sum(nums2) - sum(nums1)
    if Diff < 0:
        Diff = -Diff
        nums1, nums2 = nums2, nums1

    Res, Cnt = 0, Counter(6 - num for num in nums1) + Counter(num - 1 for num in nums2)
    for item in range(5, 0, -1):
        if item * Cnt[item] >= Diff:
            return Res + (Diff + item - 1) // item
        Res += Cnt[item]
        Diff -= item * Cnt[item]
