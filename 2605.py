from typing import List


def minNumber(nums1: List[int], nums2: List[int]) -> int:
    nums1, nums2 = sorted(nums1), sorted(nums2)
    for index_i in range(len(nums1)):
        for index_j in range(len(nums2)):
            if nums1[index_i] == nums2[index_j]:
                return nums1[index_i]
    return min(nums1[0], nums2[0]) * 10 + max(nums1[0], nums2[0])