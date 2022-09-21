"""Класс калькулятора
Создайте класс Calculator который поддерживает:

- сложение двух чисел
- вычисление разницы между двумя числами
- умножение двух чисел
- деление одного числа на другое

Примеры вызовов и возвратов из функций:

calculator = Calculator()
calculator.add(10, 5) ➞ 15
calculator.subtract(10, 5) ➞ 5
calculator.multiply(10, 5) ➞ 50
calculator.divide(10, 5) ➞ 2"""


class Calculator:

    def __init__(self, a, b):

        self.a = a

        self.b = b

    def add(self):

        return self.a + self.b

    def subtract(self):

        return self.a - self.b

    def multiply(self):

        return self.a * self.b

    def divide(self):

        return self.a / self.b
