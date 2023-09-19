from typing import List
from bisect import bisect_left


def minCapability(nums: List[int], k: int) -> int:
    def func(y):
        count, visited = 0, False
        for x in nums:
            if x <= y and not visited:
                count, visited = count + 1, True
            else:
                visited = False
        return count

    return bisect_left(range(min(nums), max(nums)), k, key=func) + min(nums)
