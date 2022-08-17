def smallestNumber(pattern: str) -> str:
    Res = []
    Chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    Temp = ""

    def BackTrace(Index):
        nonlocal Temp
        if Index == len(pattern):
            Res.append(int(Temp))
            return
        for char in Chars:
            if pattern[Index] == "I" and int(char) > int(Temp[-1]) and char not in Temp:
                Temp = Temp + char
                BackTrace(Index + 1)
                Temp = Temp[:-1]
            if pattern[Index] == "D" and int(char) < int(Temp[-1]) and char not in Temp:
                Temp = Temp + char
                BackTrace(Index + 1)
                Temp = Temp[:-1]

    for Char in Chars:
        Temp = Temp + Char
        BackTrace(0)
        Temp = Temp[:-1]

    return min(Res)


if __name__ == "__main__":
    s = "123"
    print(smallestNumber("IIIDIDDD"))
