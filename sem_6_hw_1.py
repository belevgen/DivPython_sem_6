# Задание 2
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

# def _check_leap(year: int) -> bool:
#     return year % 400 == 0 or year % 4 == 0 and year % 100 != 0
#
#
# def is_exist_date(date: str) -> bool:
#     day, month, year = (int(el) for el in date.split("."))
#     if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
#         return False
#     if month in (4, 6, 9, 11) and day > 30:
#         return False
#     if month == 2 and day > 29:
#         return False
#     if month == 2 and day == 29 and not _check_leap(year):
#         return False
#     return True
#
# if __name__ == "__main__":
#     print(is_exist_date("15.22.1967"))

import argparse

def _check_leap(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def is_exist_date(date: str) -> bool:
    day, month, year = (int(el) for el in date.split("."))
    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    if month == 2 and day > 29:
        return False
    if month == 2 and day == 29 and not _check_leap(year):
        return False
    return True

if __name__ == "__main__":
    # print(is_exist_date("15.22.1967"))

    parser = argparse.ArgumentParser(description="Проверьте существует ли дата")
    parser.add_argument("date", type=str, help="Дата в формате 'день.месяц.год'")

    args = parser.parse_args()
    result = is_exist_date(args.date)

    if result:
        print(f"Дата {args.date} существует.")
    else:
        print(f"Дата {args.date} не существует.")
