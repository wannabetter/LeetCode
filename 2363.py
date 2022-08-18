from typing import List


def mergeSimilarItems(items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    Res = []
    items1.sort()
    items2.sort()
    Top, Bot = 0, 0
    while Top < len(items1) and Bot < len(items2):
        if items1[Top][0] == items2[Bot][0]:
            Res.append([items1[Top][0], items1[Top][1] + items2[Bot][1]])
            Top += 1
            Bot += 1
        elif items1[Top][0] > items2[Bot][0]:
            Res.append(items2[Bot])
            Bot += 1
        else:
            Res.append(items1[Top])
            Top += 1
    while Top < len(items1):
        Res.append(items1[Top])
        Top += 1
    while Bot < len(items2):
        Res.append(items2[Bot])
        Bot += 1
    return Res


if __name__ == "__main__":
    print(mergeSimilarItems([[5, 1], [4, 2], [3, 3], [2, 4], [1, 5]], [[7, 1], [6, 2], [5, 3], [4, 4]]))
