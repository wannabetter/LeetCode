from math import inf


def areNumbersAscending(s: str) -> bool:
    Temp = -1
    Chars = s.split(" ")
    for char in Chars:
        if char.isdigit():
            if Temp < int(char):
                Temp = int(char)
            else:
                return False
    return True
