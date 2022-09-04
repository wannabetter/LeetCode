from functools import lru_cache


def numberOfWays(startPos: int, endPos: int, k: int) -> int:
    @lru_cache(None)
    def DFS(Index, Rest):
        if Rest == 0:
            return 1 if Index == endPos else 0
        return (DFS(Index + 1, Rest - 1) + DFS(Index - 1, Rest - 1)) % (10 ** 9 + 7)

    return DFS(startPos, k)


if __name__ == '__main__':
    print(numberOfWays(2, 5, 10))
