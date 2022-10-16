from typing import List


# 图论告诉我们奇数还没有二分图用这个做
def possibleBipartition(n: int, dislikes: List[List[int]]) -> bool:
    Colors = [-1] * n
    Maps = [[] for _ in range(n)]

    def DFS(Index):
        DisLike = Maps[Index]
        for Y in DisLike:
            if Colors[Y] == -1:
                Colors[Y] = 1 - Colors[Index]
                if not DFS(Y):
                    return False
            elif Colors[Y] == Colors[Index]:
                return False
        return True

    for dislike in dislikes:
        X, Y = dislike[0] - 1, dislike[1] - 1
        Maps[X].append(Y)
        Maps[Y].append(X)

    for Index in range(0, n):
        if Colors[Index] == -1:
            Colors[Index] = 0
            if not DFS(Index):
                return False
    return True
