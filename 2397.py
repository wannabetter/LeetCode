from typing import List
from functools import reduce


def maximumRows(matrix: List[List[int]], numSelect: int) -> int:
    rows = []
    for row in matrix:
        mask = reduce(lambda x, y: x | y, (1 << j for j, x in enumerate(row) if x), 0)
        rows.append(mask)

    ans = 0
    for mask in range(1 << len(matrix[0])):
        if mask.bit_count() != numSelect:
            continue
        t = sum((x & mask) == x for x in rows)
        ans = max(ans, t)
    return ans
