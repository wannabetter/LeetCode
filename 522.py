from typing import List


def findLUSlength(strs: List[str]) -> int:
    def SubSeq(s: str, t: str) -> bool:
        Pti, Ptj = 0, 0
        while Pti < len(s) and Ptj < len(t):
            if s[Pti] == t[Ptj]:
                Pti += 1
            Ptj += 1
        return Pti == len(s)

    ans = -1
    for index, chars in enumerate(strs):
        check = True
        for item in range(index + 1, len(strs)):
            if SubSeq(chars, strs[item]):
                check = False
                break
        if check:
            ans = max(ans, len(chars))
    return ans
