def numTilings(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        DP = [0] * (n + 1)
        DP[0] = DP[1] = 1
        DP[2] = 2
        for Index in range(3, n + 1):
            DP[Index] = DP[Index - 2] * 2 + DP[Index - 3]
        return DP[-1]
