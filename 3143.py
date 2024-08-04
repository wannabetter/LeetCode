from typing import List
from collections import Counter
from heapq import heappop, heappush


class Solution:
    def __init__(self):
        self.chars = [chr(ord('a') + length) for length in range(26)]

    def check(self, cnt: Counter) -> bool:
        for char in self.chars:
            if cnt[char] > 1:
                return False
        return True

    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        heap = []
        cnt = Counter(s)

        for index, vec in enumerate(points):
            heappush(heap, (-max(abs(vec[0]), abs(vec[-1])), index))

        while not self.check(cnt):
            length, index = -heap[0][0], heap[0][-1]

            while heap and length <= -heap[0][0]:
                cnt[s[heap[0][-1]]] -= 1
                heappop(heap)

        return len(heap)