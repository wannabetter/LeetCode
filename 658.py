from typing import List


def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    L, R, Res = 0, len(arr) - 1, []
    while L <= R:
        a, b = arr[L], arr[R]
        a_x, b_x = abs(a - x), abs(b - x)
        if a_x <= b_x:
            Temp = b
            R -= 1
        else:
            Temp = a
            L += 1
        if len(Res) < k:
            Res.append(Temp)
        else:
            Res.pop(0)
            Res.append(Temp)
    Res.sort()
    return Res


if __name__ == "__main__":
    print(findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))
