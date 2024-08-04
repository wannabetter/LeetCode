from typing import List
from heapq import heappush, heappop


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans, heap = list(), list()

        for index in range(k):
            heappush(heap, [-nums[index], index])

        ans.append(-heap[0][0])
        for index in range(k, len(nums)):
            heappush(heap, [-nums[index], index])

            while heap[0][1] <= index - k:
                heap.pop(0)

            ans.append(-heap[0][0])
        return ans
