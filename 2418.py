from typing import List


def sortPeople(names: List[str], heights: List[int]) -> List[str]:
    arr = list(zip(names, heights))
    arr = sorted(arr, key=lambda x: x[1],reverse=True)
    return [name for name,_ in arr]