from typing import List


def hIndex(citations: List[int]) -> int:
    citations.sort(reverse=True)
    left, right = 0, len(citations) - 1
    while left < right:
        mid = (left + right + 1) // 2
        if citations[mid] >= mid + 1:
            left = mid
        else:
            right = mid - 1
    if citations[left] == 0:
        return 0
    return left + 1


