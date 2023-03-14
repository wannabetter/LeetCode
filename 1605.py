from typing import List


def restoreMatrix(rowSum: List[int], colSum: List[int]) -> List[List[int]]:
    n, m = len(rowSum), len(colSum)
    mat = [[0] * m for _ in range(n)]
    for indexI, row in enumerate(rowSum):
        for indexJ, col in enumerate(colSum):
            mat[indexI][indexJ] = temp = min(row, col)
            row -= temp
            colSum[indexJ] -= temp
    return mat
