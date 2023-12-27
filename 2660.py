from typing import List


def isWinner(player1: List[int], player2: List[int]) -> int:
    score1, score2 = 0, 0
    double, temp = False, 0
    for play1 in player1:
        if not double:
            score1 += play1
        else:
            score1 += play1 * 2
            temp = (temp + 1) % 2
            double = False if temp == 0 else True
        if play1 == 10:
            double = True
            temp = 0
    double, temp = False, 0
    for play2 in player2:
        if not double:
            score2 += play2
        else:
            score2 += play2 * 2
            temp = (temp + 1) % 2
            double = False if temp == 0 else True
        if play2 == 10:
            double = True
            temp = 0
    return 1 if score1 > score2 else 0 if score1 == score2 else 2