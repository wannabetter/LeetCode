from typing import List
from heapq import heappush, heappop


def halveArray(nums: List[int]) -> int:
    ans = 0
    temp = arr_sum = sum(nums)

    heap = []
    for num in nums:
        heappush(heap, -num)

    while temp > arr_sum / 2:
        num = -heappop(heap)
        num = num / 2
        temp -= num
        ans += 1
        heappush(heap, -num)
    return ans
