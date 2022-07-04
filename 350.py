from typing import List
from collections import Counter


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    cnt = Counter()
    ans = []
    for num1 in nums1:
        cnt[num1] = cnt[num1] + 1
    for num2 in nums2:
        if cnt[num2] != 0:
            ans.append(num2)
            cnt[num2] = cnt[num2] - 1
    return ans


if __name__ == "__main__":
    intersect(nums1=[1, 2, 2, 1], nums2=[2, 2])
