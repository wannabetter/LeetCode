from typing import List
from heapq import heappush, heappop
from math import sqrt


def pickGifts(gifts: List[int], k: int) -> int:
    heap = []
    for gift in gifts:
        heappush(heap, -gift)
    for _ in range(k):
        gift = -heappop(heap)
        gift = int(sqrt(gift))
        heappush(heap, -gift)
    print(heap)
    return -sum(heap)
