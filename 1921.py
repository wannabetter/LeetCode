from typing import List


def eliminateMaximum(dist: List[int], speed: List[int]) -> int:
    ans, heap = 0, [dist[index] / speed[index] for index in range(len(dist))]
    heap.sort()
    for index, item in enumerate(heap):
        if index < item:
            ans = ans + 1
        else:
            break
    return ans
