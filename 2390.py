def removeStars(s: str) -> str:
    Res = ""
    for char in s:
        if char != '*':
            Res = Res + char
        else:
            Res = Res[:-1]
    return Res
