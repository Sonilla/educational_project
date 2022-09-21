"""Даны две даты — левая и правая границы диапазона соответственно. Напишите программу, которая из этого диапазона,
включая границы, выводит, начиная с даты, у которой сумма дня и месяца нечетная, каждую третью дату, только если она
не понедельник и не четверг.

Формат входных данных На вход программе подаются две даты в формате DD.MM.YYYY — левая и правая границы диапазона
соответственно, каждая на отдельной строке. Гарантируется, что первая дата не больше второй.

Формат выходных данных Программа должна из указанного диапазона, включая концы, вывести, начиная с даты,
у которой сумма дня и месяца нечетная, каждую третью дату, только если она не понедельник и не четверг. Даты должны
быть расположены каждая на отдельной строке, в формате DD.MM.YYYY.

Примечание 1. Если дат, удовлетворяющих условию, нет, программа ничего не должна выводить.

Примечание 2. Рассмотрим второй тест. Левая граница диапазона 07.03.2021 не является начальной датой, так как имеет
четную сумму дня и месяца, поэтому в качестве начальной берем следующую дату 08.03.2021. Дата 08.03.2021 не
выводится, так как является понедельником, поэтому двигаемся к следующей дате с шагом три: 11.03.2021. Дата
11.03.2021 не выводится, так как является четвергом. """

from datetime import date, datetime


def the_most_understendable_condition(date1: str, date2: str) -> list:
    date1, date2 = datetime.strptime(date1, '%d.%m.%Y'), datetime.strptime(date2, '%d.%m.%Y')
    res = []
    odd = False
    c = 3
    for d in range(date.toordinal(date1), date.toordinal(date2) + 1):
        d = date.fromordinal(d)
        if (d.month + d.day) % 2 == 1:
            odd = True
        if odd:
            if d.weekday() not in (0, 3) and c % 3 == 0:
                res.append(d.strftime('%d.%m.%Y'))
            c += 1
    return res
