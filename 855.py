from bisect import insort


class ExamRoom:

    def __init__(self, n: int):
        self.N = n
        self.Student = []

    def seat(self) -> int:
        if not self.Student:
            student = 0
        else:
            dist, student = self.Student[0], 0
            for index, pos in enumerate(self.Student):
                if index:
                    Prev = self.Student[index - 1]
                    d = (pos - Prev) // 2
                    if d > dist:
                        dist, student = d, Prev + d
            d = self.N - 1 - self.Student[-1]
            if d > dist:
                student = self.N - 1
            insort(self.Student, student)

        return student

    def leave(self, p: int) -> None:
        self.Student.remove(p)
