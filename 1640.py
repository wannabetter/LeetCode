from typing import List


def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
    Cnt = {}
    for index, piece in enumerate(pieces):
        Cnt[piece[0]] = index
    Index = 0
    while Index < len(arr):
        if arr[Index] not in Cnt:
            return False
        P = pieces[Cnt[arr[Index]]]
        if arr[Index:Index + len(P)] != P:
            return False
        Index += len(P)
    return True
