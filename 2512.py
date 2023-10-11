from typing import List


def topStudents(positive_feedback: List[str], negative_feedback: List[str], report: List[str],
                student_id: List[int], k: int) -> List[int]:
    words = {}
    for w in positive_feedback:
        words[w] = 3
    for w in negative_feedback:
        words[w] = -1
    temp = []
    for s, i in zip(report, student_id):
        score = sum(words.get(w, 0) for w in s.split())
        temp.append([-score, i])
    temp.sort()
    return [i for v, i in temp[:k]]
