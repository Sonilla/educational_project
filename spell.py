"""Реализуйте функцию spell(), которая принимает произвольное количество позиционных аргументов-слов и возвращает
словарь, ключи которого — первые буквы слов, а значения — максимальные длины слов на эту букву.

Примечание 1. Если в функцию не передается ни одного аргумента, функция должна возвращать пустой словарь.

Примечание 2. Функция должна игнорировать регистр слов, при этом в результирующий словарь должны попасть именно буквы
в нижнем регистре.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию, но не код, вызывающий ее. """


def spell(*args):
    if len(args) == 0:
        return {}
    chars = set(map(lambda x: x.lower()[0], args))
    d = {}
    for char in chars:
        d[char] = len(max(filter(lambda x: x.lower()[0] == char, args), key=len))
    return d
