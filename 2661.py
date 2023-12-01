from typing import List


def firstCompleteIndex(arr: List[int], mat: List[List[int]]) -> int:
    n, m = len(mat), len(mat[0])
    maps = {}
    for i in range(n):
        for j in range(m):
            maps[mat[i][j]] = [i, j]
    rowCnt, colCnt = [0] * n, [0] * m
    for index, pos in enumerate(arr):
        v = maps[pos]
        rowCnt[v[0]] += 1
        if rowCnt[v[0]] == m:
            return index
        colCnt[v[1]] += 1
        if colCnt[v[1]] == n:
            return index
    return -1