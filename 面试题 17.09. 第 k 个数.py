def getKthMagicNumber(k: int) -> int:
    DP = [1]
    P3, P5, P7 = 0, 0, 0
    for index in range(k - 1):
        Num3, Num5, Num7 = DP[P3] * 3, DP[P5] * 5, DP[P7] * 7
        Min = min(Num3, Num5, Num7)
        if Min == Num3:
            P3 += 1
        if Min == Num5:
            P5 += 1
        if Min == Num7:
            P7 += 1
        DP.append(Min)
    return DP[-1]
