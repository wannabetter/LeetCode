def isRobotBounded(instructions: str) -> bool:
    dire, x, y = 0, 0, 0
    for instruction in instructions:
        if instruction == 'L':
            dire = ((dire - 1) + 4) % 4
        elif instruction == 'R':
            dire = ((dire + 1) + 4) % 4
        else:
            if dire == 0:
                y += 1
            elif dire == 1:
                x += 1
            elif dire == 2:
                y -= 1
            else:
                x -= 1
    return dire != 0 or (x == 0 and y == 0)