from typing import List


def ambiguousCoordinates(s: str) -> List[str]:
    Res = []
    Chars = s[1:-1]

    for Index in range(1, len(Chars)):

        LeftList, RightList = [], []
        Left, Right = Chars[:Index], Chars[Index:]

        if Left[0] != "0" or Left == "0":
            LeftList.append(Left)

        if Right[0] != "0" or Right == "0":
            RightList.append(Right)

        for Idx in range(1, len(Left)):
            L, R = Left[:Idx], Left[Idx:]
            if L[0] == "0" and len(L) != 1:
                continue
            if R[-1] == "0":
                continue
            LeftList.append(L + "." + R)

        for Idx in range(1, len(Right)):
            L, R = Right[:Idx], Right[Idx:]
            if L[0] == "0" and len(L) != 1:
                continue
            if R[-1] == "0":
                continue
            RightList.append(L + "." + R)

        for left in LeftList:
            for right in RightList:
                Res.append("(" + left + ", " + right + ")")

    return Res

if __name__ == '__main__':
    print(ambiguousCoordinates("(0123)"))
