from typing import List


def countStudents(students: List[int], sandwiches: List[int]) -> int:
    Index = 0
    while Index < len(students):
        Temp = students.pop(0)
        if Temp == sandwiches[0]:
            Index = 0
            sandwiches.pop(0)
        else:
            Index += 1
            students.append(Temp)
    return len(students)
