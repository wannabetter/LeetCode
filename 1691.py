from typing import List


def maxHeight(cuboids: List[List[int]]) -> int:
    Res, DP = 0, [0] * len(cuboids)
    for cuboid in cuboids:
        cuboid.sort()
    cuboids.sort(key=sum)
    for IndexI in range(len(cuboids)):
        DP[IndexI] = cuboids[IndexI][2]
        for IndexJ in range(IndexI):
            if cuboids[IndexI][0] >= cuboids[IndexJ][0] and cuboids[IndexI][1] >= cuboids[IndexJ][1] and \
                    cuboids[IndexI][2] >= cuboids[IndexJ][2]:
                DP[IndexI] = max(DP[IndexI], DP[IndexJ] + cuboids[IndexI][2])
        Res = max(Res, DP[IndexI])
    return Res
