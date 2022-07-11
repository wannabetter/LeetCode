from typing import List
import copy


def combine(n: int, k: int) -> List[List[int]]:
    Res = []
    Path = []

    def BackTrace(Nums, LenRes, StartIndex):
        if len(Path) == LenRes:
            Res.append(copy.deepcopy(Path))
            return
        for i in range(StartIndex, Nums+1):
            Path.append(i)
            BackTrace(Nums, LenRes, i + 1)
            Path.pop()

    BackTrace(n, k, 1)
    return Res


if __name__ == "__main__":
    print(combine(4, 2))
