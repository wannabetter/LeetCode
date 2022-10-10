from typing import List


def minSwap(nums1: List[int], nums2: List[int]) -> int:
    DP0, DP1 = [0] + [len(nums1)] * (len(nums1) - 1), [1] + [len(nums1)] * (len(nums1) - 1)
    Index = 1
    while Index < len(nums1):
        if nums1[Index] > nums1[Index - 1] and nums2[Index] > nums2[Index - 1]:
            DP0[Index] = min(DP0[Index], DP0[Index - 1])
            DP1[Index] = min(DP1[Index], DP1[Index - 1] + 1)
        if nums1[Index] > nums2[Index - 1] and nums2[Index] > nums1[Index - 1]:
            DP0[Index] = min(DP0[Index], DP1[Index - 1])
            DP1[Index] = min(DP1[Index], DP0[Index - 1] + 1)
        Index += 1
    return min(DP1[-1], DP0[-1])
