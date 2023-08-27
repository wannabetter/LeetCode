from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda item: item[0])

    ans = []
    for start, end in intervals:
        if not ans or ans[-1][1] < start:
            ans.append([start, end])
        else:
            ans[-1][1] = max(ans[-1][1], end)
    return ans

