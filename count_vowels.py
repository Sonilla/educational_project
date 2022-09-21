"""Напишите функцию count_vowels, которая принимает строку и возвращает количество гласных в ней.

Примеры вызовов и возвратов:

count_vowels('abcd') -> 1
count_vowels('abcdef') -> 2
count_vowels('bcd') -> 0

Примечание: речь идёт только о латинском алфавите."""


def count_vowels(string):
    res = 0
    for ch in string:
        if ch in 'eyuioa':
            res += 1
    return res
