from typing import List


def haveConflict(event1: List[str], event2: List[str]) -> bool:
    def Time2Num(time):
        hour, minute = list(map(int, time.split(":")))
        return hour * 60 + minute

    event1 = [Time2Num(event1[0]), Time2Num(event1[1])]
    event2 = [Time2Num(event2[0]), Time2Num(event2[1])]
    return True if event2[0] <= event1[1] <= event2[1] or event1[0] <= event2[1] <= event1[1] else False
