from copy import deepcopy


def minOperations(s: str) -> int:
    Chars, Res1, Res2 = list(s), 0, 0
    Temp = deepcopy(Chars)
    for Index in range(1, len(Chars)):
        if Temp[Index - 1] == Temp[Index]:
            Res1 += 1
            Temp[Index] = '0' if Temp[Index - 1] == '1' else '1'

    Temp = deepcopy(Chars)
    Temp[0] = '0' if Temp[0] == '1' else '1'
    Res2 += 1
    for Index in range(1, len(Chars)):
        if Temp[Index - 1] == Temp[Index]:
            Res2 += 1
            Temp[Index] = '0' if Temp[Index - 1] == '1' else '1'
    return min(Res1, Res2)


if __name__ == '__main__':
    print(minOperations("10010100"))
