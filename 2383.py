from typing import List


def minNumberOfHours(initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
    consume = 0
    if initialEnergy <= sum(energy):
        consume += sum(energy) - initialEnergy + 1
    for exp in experience:
        if initialExperience > exp:
            initialExperience += exp
        else:
            consume += exp - initialExperience + 1
            initialExperience += exp - initialExperience + 1
            initialExperience += exp

    return consume


if __name__ == "__main__":
    print(minNumberOfHours(100,
                           100,
                           [1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [1, 2, 3, 1, 2, 3, 1, 2, 10]))
