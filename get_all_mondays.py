"""Реализуйте функцию get_all_mondays(), которая принимает один аргумент:

year — натуральное число Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) года
year, выпадающих на понедельник.

Примечание 1. Например, вызов:

get_all_mondays(2021)
должен вернуть список:

[datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ..., datetime.date(2021, 12, 20), datetime.date(2021, 12,
27)] """

import calendar
from datetime import date


def get_all_mondays(year: int) -> list:
    monday_list = []
    for m in range(1, 12 + 1):
        for d in range(1, calendar.monthrange(year, m)[1] + 1):
            if calendar.weekday(year, m, d) == 0:
                monday_list.append(date(year, m, d))
    return monday_list
