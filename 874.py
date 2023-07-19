from typing import List


def robotSim(commands: List[int], obstacles: List[List[int]]) -> int:
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    x, y, d = 0, 0, 1
    maps = set([tuple(i) for i in obstacles])
    ans = 0
    for command in commands:
        if command < 0:
            d += 1 if command == -1 else -1
            d = d % 4
        else:
            for i in range(command):
                if tuple([x + dirs[d][0], y + dirs[d][1]]) in maps:
                    break
                x, y = x + dirs[d][0], y + dirs[d][1]
                ans = max(ans, x * x + y * y)
    return ans
