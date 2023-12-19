from typing import List


def findPeakGrid(mat: List[List[int]]) -> List[int]:
    m = len(mat)
    low, high = 0, m - 1
    while low <= high:
        mid = (low + high) // 2
        index = mat[mid].index(max(mat[mid]))
        if mid - 1 >= 0 and mat[mid][index] < mat[mid - 1][index]:
            high = mid - 1
            continue
        if mid + 1 < m and mat[mid][index] < mat[mid + 1][index]:
            low = mid + 1
            continue
        return [mid, index]
    return None
