from typing import List
from collections import deque


def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    dist = [[0] * n for _ in range(m)]
    ZerosPos = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]
    Queue = deque(ZerosPos)
    Seen = set(ZerosPos)

    while Queue:
        row, col = Queue.popleft()
        for i, j in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if 0 <= i < m and 0 <= j < n and (i, j) not in Seen:
                dist[i][j] = dist[row][col] + 1
                Queue.append((i, j))
                Seen.add((i, j))

    return dist
