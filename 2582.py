
def passThePillow(n: int, time: int) -> int:
    time %= (n - 1) * 2
    return time + 1 if time < n else n * 2 - time - 1
