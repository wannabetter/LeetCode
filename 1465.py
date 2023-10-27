from typing import List


def maxArea(h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
    verticalCuts = [0] + sorted(verticalCuts) + [w]
    horizontalCuts = [0] + sorted(horizontalCuts) + [h]
    v_max, h_max = -1, -1
    for index in range(1, len(verticalCuts)):
        v_max = max(v_max, verticalCuts[index] - verticalCuts[index - 1])
    for index in range(1, len(horizontalCuts)):
        h_max = max(h_max, horizontalCuts[index] - horizontalCuts[index - 1])
    return h_max * v_max % (10 ** 9 + 7)