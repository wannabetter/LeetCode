def maxValue(n: int, index: int, maxSum: int) -> int:
    def SumPart(Max, Cnt):
        if Max >= Cnt:
            return (Max + Max - Cnt + 1) * Cnt / 2
        else:
            return (Max + 1) * Max / 2 + Cnt - Max

    Left, Right = 1, maxSum
    while Left < Right:
        Mid = (Left + Right+1) // 2
        if SumPart(Mid - 1, index) + SumPart(Mid, n - index) <= maxSum:
            Left = Mid
        else:
            Right = Mid - 1
    return Left
