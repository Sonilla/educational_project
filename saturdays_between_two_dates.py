"""Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:

start — начальная дата, тип date
end — конечная дата, тип date
Функция должна возвращать количество суббот между датами start и end включительно.

Примечание 1. Даты могут передаваться в любом порядке, то есть не гарантируется, что первая дата меньше второй.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию
saturdays_between_two_dates(), но не код, вызывающий ее. """

from datetime import date


def saturdays_between_two_dates(start, end):
    res = 0
    if start > end:
        start, end = end, start
    for d in range(start.toordinal(), end.toordinal() + 1):
        s = date.fromordinal(d)
        if s.weekday() == 5:
            res += 1
    return res
