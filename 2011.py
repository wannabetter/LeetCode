from typing import List


def finalValueAfterOperations(operations: List[str]) -> int:
    Sum = 0
    for Char in operations:
        if Char == "++X" or Char == "X++":
            Sum += 1
        else:
            Sum -= 1
    return Sum
