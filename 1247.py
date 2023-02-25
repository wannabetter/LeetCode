def minimumSwap(s1: str, s2: str) -> int:
    xY, yX = 0, 0
    for char1, char2 in zip(s1, s2):
        if char1 > char2:
            yX += 1
        if char1 < char2:
            xY += 1
    if (xY + yX) % 2 != 0:
        return -1
    return xY // 2 + yX // 2 + xY % 2 + yX % 2