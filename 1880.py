def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    def GetNum(Chars):
        Sum = 0
        for Char in Chars:
            Sum = Sum * 10 + (ord(Char) - 97)
        return Sum

    return GetNum(firstWord) + GetNum(secondWord) == GetNum(targetWord)
