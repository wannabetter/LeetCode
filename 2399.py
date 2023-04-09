from typing import List


def checkDistances(s: str, distance: List[int]) -> bool:
    charSet = dict()
    for index, char in enumerate(s):
        if char not in charSet.keys():
            charSet[char] = index
        else:
            if distance[ord(char) - ord('a')] != index - charSet[char] - 1:
                return False
    return True
