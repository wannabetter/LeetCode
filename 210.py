from typing import List
from collections import defaultdict


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    ans = []
    valid = True
    visited = [0] * numCourses
    maps = defaultdict(list)
    for cour1, cour2 in prerequisites:
        maps[cour2].append(cour1)

    def dfs(u: int):
        nonlocal valid
        visited[u] = 1
        for v in maps[u]:
            if visited[v] == 0:
                dfs(v)
                if not valid:
                    return
            elif visited[v] == 1:
                valid = False
                return
        visited[u] = 2
        ans.append(u)

    for index in range(numCourses):
        if valid and not visited[index]:
            dfs(index)
            if len(ans) == numCourses:
                return ans[::-1]
    return []
