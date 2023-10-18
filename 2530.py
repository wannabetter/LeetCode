from typing import List
from math import ceil
from heapq import heappush, heappop, heapify


def maxKelements(nums: List[int], k: int) -> int:
    ans = 0
    heap = []
    for num in nums:
        heappush(heap, -num)
    for _ in range(k):
        num = -heappop(heap)
        ans += num
        num = ceil(num / 3)
        heappush(heap, -num)
    return ans
