def reverseBits(n: int) -> int:
    Res = 0
    for index in range(0, 32):
        Res = Res | ((n & 1) << (31 - index))
        n = n >> 1
    return Res
