from typing import List
from collections import Counter


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        ans, n = 0, len(candyType)
        cnt = Counter(candyType)

        return n // 2 if len(cnt.keys()) > n // 2 else len(cnt.keys())
