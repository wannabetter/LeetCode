from typing import List


def buildArray(target: List[int], n: int) -> List[str]:
    Index, Idx, Res = 0, 1, []
    while Index < len(target) and Idx <= n:
        if target[Index] == Idx:
            Index += 1
            Idx += 1
            Res.append("Push")
        else:
            Res.append("Push")
            Res.append("Pop")
            Idx += 1
    return Res
