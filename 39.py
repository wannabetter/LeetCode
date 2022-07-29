from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    Res = []
    Temp = []

    def BackTrace(Target, Index):
        if Target == 0:
            Res.append(Temp[:])
            return
        elif Target > 0:
            for num in candidates[Index:]:
                Temp.append(num)
                BackTrace(Target - num, Index)
                Temp.pop()
                Index += 1
        else:
            return

    BackTrace(target, 0)
    return Res


if __name__ == "__main__":
    print(combinationSum(candidates=[2, 3, 6, 7], target=7))
