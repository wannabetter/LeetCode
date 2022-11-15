from typing import List
from collections import Counter


def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    Max = 0
    while truckSize and boxTypes:
        num, val = boxTypes.pop(0)
        if truckSize >= num:
            Max += num * val
            truckSize = truckSize - num
        else:
            Max += val * truckSize
            truckSize = 0
    return Max
