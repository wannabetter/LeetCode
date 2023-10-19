from typing import List
from collections import Counter


def tupleSameProduct(nums: List[int]) -> int:
    ans = 0
    n = len(nums)
    cnt = Counter([nums[i] * nums[j] for i in range(n) for j in range(i + 1, n)])
    for key,val in cnt.items():
        ans += val*(val-1)*4
    return ans