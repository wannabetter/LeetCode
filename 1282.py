from typing import List


def groupThePeople(groupSizes: List[int]) -> List[List[int]]:
    Res = []
    Temp = []
    Items = set(groupSizes)
    for Item in Items:
        for Index, Group in enumerate(groupSizes):
            if Group == Item:
                Temp.append(Index)
            if len(Temp) == Item:
                Res.append(Temp[:])
                Temp = []
    return Res
