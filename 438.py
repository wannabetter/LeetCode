from typing import List
from collections import Counter


def findAnagrams(s: str, p: str) -> List[int]:
    Index, Res = 0, []
    cnt = Counter(p)
    while Index + len(p) <= len(s):
        if cnt[s[Index]] != 0 and Counter(s[Index:Index + len(p)]) == cnt:
            Res.append(Index)
        Index = Index + 1
    return Res


if __name__ == "__main__":
    print(findAnagrams(s='abab', p="ab"))
