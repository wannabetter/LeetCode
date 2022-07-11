from typing import List


def letterCasePermutation(s: str) -> List[str]:
    Res = []

    def BackTrace(Chars, index):
        if len(Chars) == len(s):
            Res.append(Chars)
            return
        if s[index].isalpha():
            BackTrace(Chars + s[index].upper(), index + 1)
            BackTrace(Chars + s[index].lower(), index + 1)
        if s[index].isdigit():
            BackTrace(Chars + s[index], index + 1)

    BackTrace("", 0)
    return Res


if __name__ == "__main__":
    print(letterCasePermutation("a1b2"))
