def minimumMoves(s: str) -> int:
    Res, Index = 0, 0
    while Index < len(s):
        if s[Index] == 'X':
            Res += 1
            Index += 3
        else:
            Index += 1
    return Res
