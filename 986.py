from typing import List


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    if len(firstList) == 0 or len(secondList) == 0:
        return []
    else:
        Res = []
        IndexTop, IndexBottom = 0, 0
        if firstList[0][0] > secondList[0][0]:
            firstList, secondList = secondList, firstList
        while IndexTop < len(firstList) and IndexBottom < len(secondList):
            if firstList[IndexTop][1] < secondList[IndexBottom][0]:
                IndexTop = IndexTop + 1
            elif secondList[IndexBottom][1] < firstList[IndexTop][0]:
                IndexBottom = IndexBottom + 1
            elif firstList[IndexTop][0] <= secondList[IndexBottom][0] <= firstList[IndexTop][1] <= secondList[IndexBottom][1]:
                Res.append([secondList[IndexBottom][0], firstList[IndexTop][1]])
                IndexTop = IndexTop + 1
            elif secondList[IndexBottom][0] <= firstList[IndexTop][0] <= secondList[IndexBottom][1] <= firstList[IndexTop][1]:
                Res.append([firstList[IndexTop][0], secondList[IndexBottom][1]])
                IndexBottom = IndexBottom + 1
            elif firstList[IndexTop][0]<=secondList[IndexBottom][0]<secondList[IndexBottom][1] <=firstList[IndexTop][1]:
                Res.append([secondList[IndexBottom][0], secondList[IndexBottom][1]])
                IndexBottom=IndexBottom+1
            else:
                Res.append([firstList[IndexTop][0], firstList[IndexTop][1]])
                IndexTop=IndexTop+1

        return Res


if __name__ == "__main__":
    print(intervalIntersection(firstList=[[3, 5], [9, 20]],
                               secondList=[[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]]))
