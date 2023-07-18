from typing import List
from heapq import heappush, heappop


def minInterval(intervals: List[List[int]], queries: List[int]) -> List[int]:
    index_queries = list(range(len(queries)))
    index_queries.sort(key=lambda index: queries[index])
    intervals.sort(key=lambda interval: interval[0])
    queue = []
    ans = [-1] * len(queries)
    index = 0
    for idx in index_queries:
        while index < len(intervals) and intervals[index][0] <= queries[idx]:
            heappush(queue, (intervals[index][1] - intervals[index][0] + 1, intervals[index][0], intervals[index][1]))
            index = index + 1
        while queue and queue[0][2] < queries[idx]:
            heappop(queue)
        if queue:
            ans[idx] = queue[0][0]
    return ans
