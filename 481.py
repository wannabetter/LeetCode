def magicalString(n: int) -> int:
    if n < 4:
        return 1
    else:
        Sum = 1
        Index = 2
        Chars = [1, 2, 2]
        while Index < n:
            Temp = Chars[Index]
            if Temp == 1:
                Sum += 1
            if Index % 2 == 0:
                Chars.extend([1] * Temp)
            else:
                Chars.extend([2] * Temp)
            Index += 1
        return Sum
