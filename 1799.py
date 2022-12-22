from typing import List
from math import gcd


def maxScore(nums: List[int]) -> int:
    Len = len(nums)
    F = [0] * (1 << Len)
    GCDArr = [[0] * Len for _ in range(Len)]

    for IndexI in range(Len):
        for IndexJ in range(IndexI + 1, Len):
            GCDArr[IndexI][IndexJ] = gcd(nums[IndexI], nums[IndexJ])

    for K in range(1 << Len):
        Cnt = K.bit_count()
        if Cnt % 2 == 0:
            for IndexI in range(Len):
                if K >> IndexI & 1:
                    for IndexJ in range(IndexI + 1, Len):
                        if K >> IndexJ & 1:
                            F[K] = max(F[K], F[K ^ (1 << IndexI) ^ (1 << IndexJ)] + Cnt // 2 * GCDArr[IndexI][IndexJ])
    return F[-1]