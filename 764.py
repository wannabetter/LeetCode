from typing import List


def orderOfLargestPlusSign(n: int, mines: List[List[int]]) -> int:
    Ban = set(map(tuple, mines))
    Maps = [[n] * n for _ in range(n)]

    for IndexI in range(n):
        Count = 0
        for IndexJ in range(n):
            Count = 0 if (IndexI, IndexJ) in Ban else Count + 1
            Maps[IndexI][IndexJ] = min(Maps[IndexI][IndexJ], Count)

        Count = 0
        for IndexJ in range(n - 1, -1, -1):
            Count = 0 if (IndexI, IndexJ) in Ban else Count + 1
            Maps[IndexI][IndexJ] = min(Maps[IndexI][IndexJ], Count)

    for IndexJ in range(n):
        Count = 0
        for IndexI in range(n):
            Count = 0 if (IndexI, IndexJ) in Ban else Count + 1
            Maps[IndexI][IndexJ] = min(Maps[IndexI][IndexJ], Count)

        Count = 0
        for IndexI in range(n - 1, -1, -1):
            Count = 0 if (IndexI, IndexJ) in Ban else Count + 1
            Maps[IndexI][IndexJ] = min(Maps[IndexI][IndexJ], Count)

    return max(map(max, Maps))
