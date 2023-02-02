from typing import List


def shortestAlternatingPaths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    maps = [[] for _ in range(n)]
    for redX, redY in redEdges:
        maps[redX].append((redY, 0))
    for blueX, blueY in blueEdges:
        maps[blueX].append((blueY, 1))

    steps = 0
    ans = [-1] * n
    vis = [(0, 0), (0, 1)]
    queue = [(0, 0), (0, 1)]

    while queue:
        temp = queue
        queue = []

        for x, color in temp:
            if ans[x] == -1:
                ans[x] = steps
            for nextSteps in maps[x]:
                if nextSteps[1] != color and nextSteps not in vis:
                    vis.append(nextSteps)
                    queue.append(nextSteps)

        steps += 1

    return ans
