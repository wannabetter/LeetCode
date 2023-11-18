from typing import List
from collections import Counter


def maximumSum(nums: List[int]) -> int:
    ans = -1
    cnt = Counter()
    for index, num in enumerate(nums):
        num = sum(list(map(int, str(num))))
        ans = max(ans, -1 if cnt[num] == 0 else cnt[num] + nums[index])
        cnt[num] = max(cnt[num], nums[index])
    return ans