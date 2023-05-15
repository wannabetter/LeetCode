from typing import List
from collections import Counter


def maxEqualRowsAfterFlips(matrix: List[List[int]]) -> int:
    cnt = Counter()
    for row in matrix:
        if row[0]:
            for j in range(len(row)):
                row[j] ^= 1
        cnt[str(row)] += 1
    return max(cnt.values())