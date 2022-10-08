from typing import List
from math import inf


def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
    n = len(nums1)
    Idx1, Idx2 = list(range(n)), list(range(n))
    # 索引排序
    Idx1.sort(key=lambda x: nums1[x])
    Idx2.sort(key=lambda x: nums2[x])

    Res = [0] * n
    Left, Right = 0, n - 1
    for Index in range(n):
        if nums1[Idx1[Index]] > nums2[Idx2[Left]]:
            Res[Idx2[Left]] = nums1[Idx1[Index]]
            Left += 1
        else:
            Res[Idx2[Right]] = nums1[Idx1[Index]]
            Right -= 1

    return Res