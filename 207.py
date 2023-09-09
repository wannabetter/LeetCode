from typing import List
from collections import defaultdict


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    maps = defaultdict(list)
    for cour1, cour2 in prerequisites:
        maps[cour1].append(cour2)

    valid = True
    visited = [0] * numCourses

    def dfs(u):
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

    for index in range(numCourses):
        if valid and not visited[index]:
            dfs(index)

    return valid
