from typing import List
from collections import deque


def pondSizes(land: List[List[int]]) -> List[int]:
    res = []
    for index_i in range(len(land)):
        for index_j in range(len(land[0])):
            if land[index_i][index_j] == 0:
                cnt = 1
                queue = deque([(index_i, index_j)])
                land[index_i][index_j] = -1

                while queue:
                    pos_x, pos_y = queue.popleft()
                    for offset_x, offset_y in [[1, 1], [-1, -1], [-1, 1], [1, -1], [0, 1], [1, 0], [-1, 0], [0, -1]]:
                        if 0<= pos_x + offset_x<len(land) and 0 <= pos_y + offset_y < len(land[0]) and land[pos_x + offset_x][pos_y + offset_y]==0:
                            cnt += 1
                            land[pos_x + offset_x][pos_y + offset_y] = -1
                            queue.append((pos_x + offset_x, pos_y + offset_y))
                res.append(cnt)
    res.sort()
    return res