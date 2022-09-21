"""Реализуйте функцию choose_plural(), которая принимает два аргумента в следующем порядке:

amount — натуральное число, количество declensions — кортеж из трех вариантов склонения существительного Функция
должна возвращать строку, полученную путем объединения подходящего существительного из кортежа declensions и
количества amount, в следующем формате:

<количество> <существительное>"""


def choose_plural(amount: int, declensions: tuple) -> str:
    if amount == 0 or 5 <= amount <= 19 or 10 <= amount % 100 <= 19 or amount % 10 == 0:
        return f'{amount} {declensions[2]}'
    elif amount == 1 or amount % 10 == 1:
        return f'{amount} {declensions[0]}'
    elif amount in (2, 3, 4) or amount % 10 in (2, 3, 4):
        return f'{amount} {declensions[1]}'
    elif amount % 10 in (5, 6, 7, 8, 9):
        return f'{amount} {declensions[2]}'
    else:
        return f'Error: test amount = {amount}, test declensions = {declensions}'
