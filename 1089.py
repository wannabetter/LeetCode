from typing import List


def duplicateZeros(arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    Index = 0
    arrLen = len(arr)

    while Index < arrLen:
        if arr[Index] == 0:
            arr.insert(Index, 0)
            arr.pop()
            Index = Index + 1
        Index = Index + 1

    # arr = arr[0:arrLen]
    print(arr)


if __name__ == "__main__":
    duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
