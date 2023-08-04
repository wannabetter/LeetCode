from typing import List


def uniquePathsIII(grid: List[List[int]]) -> int:
    start_x, start_y, n = 0, 0, 0
    for index_x in range(len(grid)):
        for index_y in range(len(grid[0])):
            if grid[index_x][index_y] == 0:
                n = n + 1
            if grid[index_x][index_y] == 1:
                n = n + 1
                start_x, start_y = index_x, index_y

    def backtrace(cur_x, cur_y, path):
        if grid[cur_x][cur_y] == 2:
            if path == 0:
                return 1
            return 0
        temp = grid[cur_x][cur_y]
        grid[cur_x][cur_y] = -1
        ans = 0
        for add_x, add_y in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            temp_x, temp_y = cur_x + add_x, cur_y + add_y
            if 0 <= temp_x < len(grid) and 0 <= temp_y < len(grid[0]) and grid[temp_x][temp_y] in [0, 2]:
                ans += backtrace(temp_x, temp_y, path - 1)
        grid[cur_x][cur_y] = temp
        return ans

    return backtrace(start_x, start_y, n)
