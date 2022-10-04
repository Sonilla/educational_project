"""Во многих музеях существует один день месяца, когда посещение музея для всех лиц или отдельных категорий граждан
происходит без взимания платы. Например, в Эрмитаже это третий четверг месяца.

Напишите программу, которая определяет даты бесплатных дней посещения Эрмитажа в заданном году.

Формат входных данных
На вход программе подается натуральное число, представляющее год.

Формат выходных данных Программа должна определить все даты бесплатных дней посещения Эрмитажа в введенном году и
вывести их. Даты должны быть расположены в порядке возрастания, каждая на отдельной строке, в формате DD.MM.YYYY. """


import calendar
from datetime import datetime

year = int(input())

thursday_count = 0

thursday_list = []


for m in range(1, 12+1):
    f = True
    for d in range(1, calendar.monthrange(year, m)[1] + 1):
        da = (datetime(year, m, d), calendar.weekday(year, m, d))
        if calendar.weekday(year, m, d) == 3 and f:
            thursday_count += 1
        if thursday_count == 3 and f:
            thursday_count = 0
            f = False
            thursday_list.append(datetime.strftime(datetime(year, m, d), "%d.%m.%Y"))

print(*thursday_list, sep="\n")
