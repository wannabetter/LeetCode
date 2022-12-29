from typing import List
from collections import Counter


def twoOutOfThree(nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
    Cnt = Counter(set(nums1)) + Counter(set(nums2)) + Counter(set(nums3))
    Res = []
    for Key, Val in Cnt.items():
        if Val >= 2:
            Res.append(Key)
    return Res