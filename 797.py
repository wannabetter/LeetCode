from typing import List
import copy


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    Res = []

    def DFS(Index, Dist):

        if Index + 1 == len(graph):
            Res.append(Dist)
            return

        for item in graph[Index]:
            Temp = copy.deepcopy(Dist)
            Temp.append(item)
            DFS(item, Temp)

    DFS(0, [0])

    return Res


if __name__ == "__main__":
    print(allPathsSourceTarget([[1, 2], [3], [3], []]))
