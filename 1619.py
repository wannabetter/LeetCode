from typing import List


def trimMean(arr: List[int]) -> float:
    arr.sort()
    arr = arr[int(len(arr) * 0.05):-int(len(arr) * 0.05)]
    return round(sum(arr) / len(arr), 5)


if __name__ == '__main__':
    print(trimMean(
        [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10,
         8, 2, 3, 4]))
