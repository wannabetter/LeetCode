from typing import List
from collections import defaultdict


def checkIfPrerequisite(numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    ans = []
    maps = defaultdict(list)
    for cour1, cour2 in prerequisites:
        maps[cour2].append(cour1)
    for end, start in queries:
        visited = [False] * numCourses

        def dfs(u):
            nonlocal visited
            for v in maps[u]:
                if not visited[v]:
                    visited[v] = True
                    dfs(v)

        dfs(start)
        if visited[end]:
            ans.append(True)
        else:
            ans.append(False)
    return ans