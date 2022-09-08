from typing import List


def constructArray(n: int, k: int) -> List[int]:
    Index, P, Q, Res = 0, 1, n, []
    while Index < k:
        if Index % 2 == 0:
            Res.append(P)
            P += 1
        else:
            Res.append(Q)
            Q -= 1
        Index += 1
    if k % 2 == 0:
        while Index < n:
            Res.append(Q)
            Q -= 1
            Index += 1
    else:
        while Index < n:
            Res.append(P)
            P += 1
            Index += 1
    return Res


if __name__ == '__main__':
    print(constructArray(3, 1))
