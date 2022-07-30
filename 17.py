from typing import List


def letterCombinations(digits: str) -> List[str]:
    if digits == "":
        return []

    Res = []

    def GetChar(CharNum):
        if CharNum == "2":
            return ['a', 'b', 'c']
        elif CharNum == "3":
            return ['d', 'e', 'f']
        elif CharNum == "4":
            return ['g', 'h', 'i']
        elif CharNum == "5":
            return ['j', 'k', 'l']
        elif CharNum == "6":
            return ['m', 'n', 'o']
        elif CharNum == "7":
            return ['p', 'q', 'r', 's']
        elif CharNum == "8":
            return ['t', 'u', 'v']
        else:
            return ['w', 'x', 'y', 'z']

    def BackTrace(Index, Chars: str):
        if Index == len(digits):
            Res.append(Chars)
            return

        Temp = GetChar(Chars[Index])
        for chars in Temp:
            Chars = Chars[:Index] + chars + Chars[Index + 1:]
            BackTrace(Index + 1, Chars)

    BackTrace(0, digits)
    return Res


if __name__ == "__main__":
    print(letterCombinations("2"))
