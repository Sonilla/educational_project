"""Написать функцию check_sequence, принимающую список целых чисел и возвращающую 1 если последовательность строго
возрастающая, -1 если строго убывающая, 0 если ни то, ни другое.

Примеры вызовов и возвратов:

check_sequence([1, 2, 3]) ➞ 1
check_sequence([3, 2, 1]) ➞ -1
check_sequence([1, 2, 1]) ➞ 0
check_sequence([1, 1, 2]) ➞ 0 # потому что 1 по индексу 1 не больше 1 по индексу 0

Примечание: входящие списки содержат минимум 2 числа."""


def check_sequence(lst) -> int:
    res = [int(x) > lst[i] for i, x in enumerate(lst[1:])]
    res1 = [int(x) < lst[i] for i, x in enumerate(lst[1:])]
    if all(res):
        return 1
    elif all(res1):
        return -1
    else:
        return 0
