from math import inf
from typing import List


def shortestSubarray(nums: List[int], k: int) -> int:
    Queue, PreSubNums, Res = [], [0], inf
    for index, num in enumerate(nums):
        PreSubNums[index + 1] = PreSubNums[index] + num
    for index, CurSum in enumerate(PreSubNums):
        while Queue and CurSum - PreSubNums[Queue[0]] >= k:
            Res = min(Res, index - Queue.pop(0))
        while Queue and CurSum <= PreSubNums[Queue[-1]]:
            Queue.pop()
        Queue.append(index)
    return -1 if Res == inf else Res
