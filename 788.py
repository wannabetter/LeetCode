def rotatedDigits(n: int) -> int:
    Sum = 0
    for Num in range(n + 1):
        Temp = list(str(Num))
        if "3" in Temp or "4" in Temp or "7" in Temp:
            continue
        if "2" in Temp or "5" in Temp or "6" in Temp or "9" in Temp:
            Sum += 1
    return Sum
