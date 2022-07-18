def backspaceCompare(s: str, t: str) -> bool:
    TempS, TempT = "", ""
    for char in s:
        if char != "#":
            TempS = TempS + char
        else:
            TempS = TempS[:-1]
    for char in t:
        if char != "#":
            TempT = TempT + char
        else:
            TempT = TempT[:-1]

    return TempS == TempT
