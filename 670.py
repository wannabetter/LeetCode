def maximumSwap(num: int) -> int:
    Nums = list(str(num))
    MaxNum = num

    def BackTrace(Index=0):
        nonlocal MaxNum
        if Index == len(Nums):
            return
        for index in range(Index + 1, len(Nums)):
            Nums[index], Nums[Index] = Nums[Index], Nums[index]
            Chars = ""
            for Num in Nums:
                Chars += Num
            MaxNum = max(MaxNum, int(Chars))
            Nums[index], Nums[Index] = Nums[Index], Nums[index]
        BackTrace(Index + 1)

    BackTrace()
    return MaxNum


if __name__ == '__main__':
    print(maximumSwap(1993))
