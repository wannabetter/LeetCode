def reorderSpaces(text: str) -> str:
    TempWords = []
    Blank = 0
    Index = 0
    Ans = ""
    while Index < len(text):
        if text[Index] == " ":
            Blank += 1
            Index += 1
        else:
            Words = ""
            while Index < len(text) and text[Index] != " ":
                Words += text[Index]
                Index += 1
            TempWords.append(Words)

    if len(TempWords) == 1:
        Token = 1
    else:
        Token = 0

    Rest = Blank % ((len(TempWords) - 1) + Token)
    Keep = Blank // ((len(TempWords) - 1) + Token)
    for Idx, Words in enumerate(TempWords):
        Ans = Ans + Words
        if Idx != (len(TempWords) - 1 + Token):
            Ans = Ans + " " * Keep

    return Ans if Rest == 0 else Ans + " " * Rest


if __name__ == '__main__':
    print(reorderSpaces("  this   is  a sentence "))
