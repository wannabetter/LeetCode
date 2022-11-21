from functools import lru_cache


def soupServings(n: int) -> float:
    N = (n + 24) // 25
    if N >= 179:
        return 1

    @lru_cache(None)
    def DFS(A, B):
        if A <= 0 and B <= 0:
            return 0.5
        elif A <= 0:
            return 1
        elif B <= 0:
            return 0
        else:
            return (DFS(A - 4, B) + DFS(A - 3, B - 1) + DFS(A - 2, B - 2) + DFS(A - 1, B - 3)) / 4

    return DFS(N, N)
