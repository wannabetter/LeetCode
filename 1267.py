from typing import List


def countServers(grid: List[List[int]]) -> int:
    def BFS(index_x, index_y):
        ret = 0
        queue = [[index_x, index_y]]
        while queue:
            cur_x, cur_y = queue.pop(0)
            grid[cur_x][cur_y] = 0
            for index in range(len(grid)):
                if grid[index][cur_y] == 1:
                    ret = ret + 1
                    grid[index][cur_y] = 0
                    if [index, cur_y] not in queue:
                        queue.append([index, cur_y])
            for index in range(len(grid[0])):
                if grid[cur_x][index] == 1:
                    ret = ret + 1
                    grid[cur_x][index] = 0
                    if [cur_x, index] not in queue:
                        queue.append([cur_x, index])
        return ret + 1 if ret != 0 else 0

    ans = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                ans += BFS(row, col)
    return ans