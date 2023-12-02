from typing import List


def carPooling(trips: List[List[int]], capacity: int) -> bool:
    diff = [0] * (max(trip[-1] for trip in trips) + 1)
    for num_i, from_i, to_i in trips:
        diff[from_i] += num_i
        diff[to_i] -= num_i
    count = 0
    for index in range(len(diff)):
        count += diff[index]
        if count > capacity:
            return False
    return True
