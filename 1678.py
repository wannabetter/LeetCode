def interpret(command: str) -> str:
    Res = ""
    Index = 0
    while Index < len(command):
        if command[Index] == "G":
            Res += command[Index]
        if command[Index] == "(":
            Temp = ""
            Index+=1
            while Index < len(command) and command[Index] != ")":
                Temp += command[Index]
                Index += 1
            if Temp == "":
                Res += "o"
            else:
                Res += Temp
        Index += 1
    return Res


if __name__ == '__main__':
    print(interpret("G()()()()(al)"))
