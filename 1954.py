def minimumPerimeter(neededApples: int) -> int:
    n = 1
    while 2 * n * (n + 1) * (2 * n + 1) < neededApples:
        n = n + 1
    return 8 * n
