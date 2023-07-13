from math import inf
from typing import List
from copy import deepcopy


def minFallingPathSum(matrix: List[List[int]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    dp = deepcopy(matrix)

    for index_y in range(1, rows):
        for index_x in range(cols):
            temp = inf
            for add_x in [-1, 0, 1]:
                if 0 <= add_x + index_x < cols:
                    temp = min(temp, matrix[index_y - 1][index_x + add_x])
            dp[index_y][index_x] += temp

    return min(min(mat for mat in matrix))
