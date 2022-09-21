"""Напишите программу, которая принимает на вход последовательность дат и проверяет каждую из них на корректность.

Формат входных данных На вход программе подается последовательность дат в формате DD.MM.YYYY, каждая на отдельной
строке. Концом последовательности является слово end.

Формат выходных данных Программа должна для каждой введенной даты вывести текст Корректная или Некорректная в
зависимости от того, является ли дата корректной, а затем вывести количество корректных дат. """

from datetime import date


def is_correct(d: int, m: int, y: int) -> bool:
    try:
        return isinstance(date(day=d, month=m, year=y), date)
    except:
        return False


correct_date_counter = 0

for input_date in iter(input, 'end'):
    if is_correct(*map(int, input_date.split('.'))):
        print('Корректная')
        correct_date_counter += 1
    else:
        print('Некорректная')
