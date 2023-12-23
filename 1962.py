from typing import List
from heapq import heappop, heappush


def minStoneSum(piles: List[int], k: int) -> int:
    heap = []
    for pile in piles:
        heappush(heap, -pile)

    for _ in range(k):
        pile = -heappop(heap)
        sub = int(pile/2)
        pile = pile - sub
        heappush(heap,-pile)
    return -sum(heap)