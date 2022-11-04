def reachNumber(target: int) -> int:
    Stride, Pos = 0, 0
    while Pos < abs(target) or (Pos - target) % 2:
        Stride += 1
        Pos += Stride
    return Stride
