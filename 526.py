def countArrangement(n: int) -> int:
    Res = 0
    Temp = []

    def BackTrace(index):
        nonlocal Res
        if index == n:
            print(Temp)
            Res += 1
        for i in range(1, n + 1):
            if i not in Temp and (i / (index+1) == int(i / (index+1)) or (index+1) / i == int((index+1) / i)):
                Temp.append(i)
                BackTrace(index + 1)
                Temp.pop()

    for i in range(1, n + 1):
        Temp.append(i)
        BackTrace(1)
        Temp.pop()
    return Res


if __name__ == "__main__":
    print(countArrangement(3))
