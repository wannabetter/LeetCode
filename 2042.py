from math import inf


def areNumbersAscending(s: str) -> bool:
    Lists = s.split(" ")
    Max = -inf
    for List in Lists:
        try:
            Num = int(List)
        except ValueError:
            continue
        else:
            if Max < Num:
                return False
            Max = Num
    return True


if __name__ == "__main__":
    print(int("ab"))
