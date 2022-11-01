from typing import List
from collections import Counter


def mostPopularCreator(creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
    Max, Index, IdxDicts, ViewDicts, N, Res = 0, 0, Counter(), Counter(), len(creators), []
    while Index < N:
        ViewDicts[creators[Index]] += views[Index]
        Max = max(Max, ViewDicts[creators[Index]])
        if creators[Index] not in IdxDicts:
            IdxDicts[creators[Index]] = Index
        else:
            if views[Index] > views[IdxDicts[creators[Index]]]:
                IdxDicts[creators[Index]] = Index
            if views[Index] == views[IdxDicts[creators[Index]]] and ids[Index] < ids[IdxDicts[creators[Index]]]:
                IdxDicts[creators[Index]] = Index
        Index += 1
    for Key in ViewDicts:
        if ViewDicts[Key] == Max:
            Res.append([Key, ids[IdxDicts[Key]]])
    return Res
