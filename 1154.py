def dayOfYear(date: str) -> int:
    year, month, day = list(map(int, date.split('-')))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        month2days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        month2days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(month2days[:month - 1]) + day
