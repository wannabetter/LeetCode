import heapq
from typing import List
from collections import Counter


def rearrangeBarcodes(barcodes: List[int]) -> List[int]:
    cnt = Counter(barcodes)
    queue = []
    for key, val in cnt.items():
        heapq.heappush(queue, (-val, key))

    res = []

    while queue:
        val, key = heapq.heappop(queue)
        if not res or res[-1] != key:
            res.append(key)
            if val < -1:
                heapq.heappush(queue, (val + 1, key))
        else:
            v, k = heapq.heappop(queue)
            res.append(k)
            if v < -1:
                heapq.heappush(queue, (v + 1, k))
            heapq.heappush(queue, (val, key))
    return res