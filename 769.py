from typing import List


def maxChunksToSorted(arr: List[int]) -> int:
    Index, Res = 0, 0
    while Index < len(arr):
        if Index != arr[Index]:
            Temp = arr[Index]
            while Index <= Temp:
                if arr[Index] > Temp:
                    Temp = arr[Index]
                Index += 1
            Res += 1
        else:
            Res += 1
            Index += 1
    return Res
