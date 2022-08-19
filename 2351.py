from math import inf


def repeatedCharacter(s: str) -> str:
    FLAG = inf
    for IndexI in range(0, len(s)):
        for IndexJ in range(IndexI + 1, len(s)):
            if s[IndexI] == s[IndexJ]:
                FLAG = min(FLAG, IndexJ)
    return s[FLAG]