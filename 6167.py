from typing import List


def checkDistances(s: str, distance: List[int]) -> bool:
    SetChars = set(s)
    Res = [0] * 26
    Flag = [False] * 26
    for index in range(26):
        if chr(ord('a') + index) not in SetChars:
            distance[ord(chr(ord('a') + index))-ord('a')] = 0
    for index, char in enumerate(s):
        if not Flag[ord(char) - ord('a')]:
            Res[ord(char) - ord('a')] = index
            Flag[ord(char) - ord('a')] = True
        else:
            Res[ord(char) - ord('a')] = index - Res[ord(char) - ord('a')] - 1
    return Res == distance


if __name__ == '__main__':
    print(ord('a') + 25)
    s = "abcda"
    p = set(s)
    print(p)
