from typing import List


def queensAttacktheKing(queens: List[List[int]], king: List[int]) -> List[List[int]]:
    ans = []
    queens = set((queen_x, queen_y) for queen_x, queen_y in queens)
    for offset_x in [-1, 0, 1]:
        for offset_y in [-1, 0, 1]:
            if offset_x == offset_y == 0:
                continue
            pos_x, pos_y = king[0] + offset_x, king[1] + offset_y
            while 0 <= pos_x < 8 and 0 <= pos_y < 8:
                if (pos_x, pos_y) in queens:
                    ans.append([pos_x, pos_y])
                    break
                pos_x += offset_x
                pos_y += offset_y
    return ans
