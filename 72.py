def minDistance(word1: str, word2: str) -> int:
    M, N = len(word1), len(word2)
    DP = [[0] * (M + 1) for _ in range(N + 1)]

    for Row in range(M + 1):
        DP[0][Row] = Row
    for Col in range(N + 1):
        DP[Col][0] = Col

    for IndexI in range(1, N + 1):
        for IndexJ in range(1, M + 1):
            Left = DP[IndexI - 1][IndexJ] + 1
            Down = DP[IndexI][IndexJ-1] + 1
            Left_Down = DP[IndexI - 1][IndexJ - 1]
            if word2[IndexI - 1] != word1[IndexJ - 1]:
                Left_Down += 1
            DP[IndexI][IndexJ] = min(Left, Down, Left_Down)

    print(DP)
    return DP[N][M]


if __name__ == "__main__":
    print(minDistance("horse", "ros"))
