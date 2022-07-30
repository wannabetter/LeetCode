from typing import List


def generateParenthesis(n: int) -> List[str]:
    Res = []

    def BackTrace(Chars, Left, Right):
        if len(Chars) == 2 * n:
            Res.append(Chars)
            return
        if Left < n:
            BackTrace(Chars + "(", Left + 1, Right)
        if Right < n and Left > Right:
            BackTrace(Chars + ")", Left, Right + 1)

    BackTrace("", 0, 0)
    return Res


if __name__ == "__main__":
    print(generateParenthesis(3))
