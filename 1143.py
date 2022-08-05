def longestCommonSubsequence(text1: str, text2: str) -> int:
    M, N = len(text1), len(text2)
    DP = [[0] * (N + 1) for _ in range(M + 1)]  # 不能[[0]*(N+1)]*(M+1)，这样会导致里面的list是相同的，相当于浅复制。
    print(DP)
    for IndexI in range(1, M + 1):
        for IndexJ in range(1, N + 1):
            if text1[IndexI - 1] == text2[IndexJ - 1]:
                DP[IndexI][IndexJ] = DP[IndexI - 1][IndexJ - 1] + 1
            else:
                DP[IndexI][IndexJ] = max(DP[IndexI][IndexJ - 1], DP[IndexI - 1][IndexJ])
    return DP[M][N]


if __name__ == "__main__":
    print(longestCommonSubsequence(text1="abcde", text2="ace"))
