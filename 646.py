from typing import List


def findLongestChain(pairs: List[List[int]]) -> int:
    Res = [1] * len(pairs)
    pairs.sort()
    for IndexI in range(len(pairs)):
        for IndexJ in range(IndexI + 1, len(pairs)):
            a, b = pairs[IndexI]
            c, d = pairs[IndexJ]
            if c > b:
                Res[IndexJ] = max(Res[IndexJ], Res[IndexI] + 1)
    return max(Res)