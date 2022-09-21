"""Назовем набор различных натуральных чисел группой. Например: (13, 4, 22, 40)(13,4,22,40). Тогда длиной группы
будем считать количество чисел в группе. Например, длина группы (13, 4, 22, 40)(13,4,22,40) равна 44.

Дана последовательность натуральных чисел от 11 до nn включительно. Напишите программу, которая группирует все числа
данной последовательности по сумме их цифр и определяет длину группы, содержащей наибольшее количество чисел.

Формат входных данных
На вход программе подается натуральное число nn.

Формат выходных данных Программа должна сгруппировать все числа из натуральной последовательности от 11 до nn по
сумме их цифр и определить длину группы, содержащей наибольшее количество чисел. """


def max_group(n: str) -> int:
    numbers = list(range(1, int(n)+1))
    res = {}
    for num in numbers:
        s = sum(map(int, list(str(num))))
        if s not in res:
            res[s] = 1
        else:
            res[s] += 1
    return max(res.values())
