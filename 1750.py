def minimumLength(s: str) -> int:
    Left, Right = 0, len(s) - 1
    while Left < Right and s[Left] == s[Right]:
        Char = s[Left]
        while Left <= Right and s[Left] == Char:
            Left += 1
        while Left <= Right and s[Right] == Char:
            Right -= 1
    return Right - Left + 1
