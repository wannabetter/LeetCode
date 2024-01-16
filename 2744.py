from copy import deepcopy
from typing import List


def maximumNumberOfStringPairs(words: List[str]) -> int:
    ans = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            temp = deepcopy(list(words[i]))
            temp.reverse()
            if temp == list(words[j]):
                ans = ans + 1
    return ans

