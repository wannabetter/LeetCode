from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    for Mats in matrix:
        for Mat in Mats:
            if Mat == target:
                return True
            if Mat > target:
                return False
    return False
