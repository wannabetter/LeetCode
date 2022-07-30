from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    Res = []
    Temp = []
    candidates.sort()

    def BackTrace(Target, Begin):
        if Target == 0:
            Res.append(Temp[:])
            return
        elif Target < 0:
            return
        else:
            for Index in range(Begin, len(candidates)):
                if Index > Begin and candidates[Index - 1] == candidates[Index]:
                    continue
                Temp.append(candidates[Index])
                BackTrace(Target - candidates[Index], Index + 1)
                Temp.pop()

    BackTrace(target, 0)
    return Res


if __name__ == "__main__":
    print(combinationSum2(
        candidates=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1], target=30))
