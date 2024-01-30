from typing import List
from collections import defaultdict


def minimumSeconds(nums: List[int]) -> int:
    ans = n = len(nums)

    mp = defaultdict(list)

    for index, val in enumerate(nums):
        mp[val].append(index)

    for pos in mp.values():
        mx = pos[0] + n - pos[-1]
        for index in range(len(pos)):
            mx = max(mx, pos[index] - pos[index - 1])
        ans = min(ans, mx // 2)
    return ans
