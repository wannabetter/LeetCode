def checkOnesSegment(s: str) -> bool:
    Chars = list(s)
    Index = 0
    Nums = 0
    while Index < len(Chars):
        if Chars[Index] == "1":
            while Index < len(Chars) and Chars[Index] == "1":
                Index += 1
            Nums += 1
        else:
            Index += 1
    return Nums <= 1
