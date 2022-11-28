from typing import List
from itertools import accumulate


def largestSumOfAverages(nums: List[int], k: int) -> float:
    PreSum = list(accumulate(nums, initial=0))

    DP = [[0.0] * (k + 1) for _ in range(len(nums) + 1)]
    for IndexI in range(1, len(nums) + 1):
        DP[IndexI][1] = PreSum[IndexI] / i
    for IndexJ in range(2, k + 1):
        for IndexI in range(IndexJ, len(nums) + 1):
            for X in range(IndexJ - 1, IndexI):
                DP[IndexI][IndexJ] = max(DP[IndexI][IndexJ],
                                         DP[X][IndexJ - 1] + (PreSum[IndexI] - PreSum[X]) / (IndexI - X))
    return DP[len(nums)][k]
