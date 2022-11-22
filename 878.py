import math


def nthMagicalNumber(n: int, a: int, b: int) -> int:
    Left, Right, LCM = min(a, b), n * min(a, b), math.lcm(a, b)
    while Left <= Right:
        Mid = (Left + Right) // 2
        Cnt = Mid // a + Mid // b - Mid // LCM
        if Cnt >= n:
            Right = Mid - 1
        else:
            Left = Mid + 1
    return (Right + 1) % (10 ** 9 + 7)
