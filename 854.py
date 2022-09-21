from math import inf


def kSimilarity(s1: str, s2: str) -> int:
    Min = inf
    Chars1, Chars2 = list(s1), list(s2)

    def BFS(Index=0, Changes=0):

        nonlocal Min
        if Changes>=Min:
            return
        if Chars1 == Chars2:
            Min = min(Min, Changes)
            return
        if Chars1[Index] == Chars2[Index]:
            BFS(Index + 1, Changes)
        else:
            for Idx in range(Index + 1, len(Chars1)):
                if Chars1[Idx] == Chars2[Index]:
                    Chars1[Idx], Chars1[Index] = Chars1[Index], Chars1[Idx]
                    BFS(Index + 1, Changes + 1)
                    Chars1[Idx], Chars1[Index] = Chars1[Index], Chars1[Idx]

    BFS()
    return Min


if __name__ == '__main__':

