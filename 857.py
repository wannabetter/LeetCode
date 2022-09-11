import heapq
from math import inf
from typing import List


def mincostToHireWorkers(quality: List[int], wage: List[int], k: int) -> float:
    ans, total, pq = inf, 0, []
    for q, w in sorted(zip(quality, wage), key=lambda x: (x[1] / x[0])):
        total += q
        heapq.heappush(pq, -q)
        if len(pq) > k:
            total += heapq.heappop(pq)
        if len(pq) == k:
            ans = min(ans, total * w / q)
    return ans


if __name__ == '__main__':
    print(mincostToHireWorkers(quality=[10, 20, 5], wage=[70, 50, 30], k=2))
