from typing import List


def findNumberIn2DArray(matrix: List[List[int]], target: int) -> bool:
    if len(matrix) == 0:
        return False
    if len(matrix[0]) == 0:
        return False
    for mat in matrix:
        if mat[0] <= target <= mat[-1]:
            if target in mat:
                return True
    return False
