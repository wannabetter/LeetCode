from typing import List


def lemonadeChange(bills: List[int]) -> bool:
    five, ten = 0, 0
    for bill in bills:
        if bill == 5:
            five = five + 1
        elif bill == 10:
            if five > 0:
                ten = ten + 1
                five = five - 1
            else:
                return False
        else:
            if five > 1 and ten > 0:
                five = five - 2
                ten = ten - 1
            else:
                return False
    return True