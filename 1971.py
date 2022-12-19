from typing import List


def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    Flag = [False] * n
    Maps = [[] * n for _ in range(n)]
    for X, Y in edges:
        Maps[Y].append(X)
        Maps[X].append(Y)

    def DFS(Index):
        if Index == destination:
            return True
        Flag[Index] = True
        for V in Maps[Index]:
            if not Flag[V] and DFS(V):
                return True
        return False

    return DFS(source)
