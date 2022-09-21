"""Создать класс Beverage, который при конструировании принимает список ингредиентов

- поддерживает атрибут ingredients, возвращающий список ингредиентов, переданных при конструировании инстанции класса

- поддерживает функцию get_cost, вычисляющую итоговую стоимость всех ингредиентов напитка (получается себестоимость напитка)

- поддерживает функцию get_price, вычисляющую цену напитка посредством умножения себестоимости на 2.5

- поддерживает функцию get_name, которая возвращает строку, перечисляющую ингредиенты, сортируя их в алфавитном
порядке. Если ингредиентов больше одного, то в конце добавляет слово 'Fusion', иначе добавляет слово 'Smoothie'. Эта
функция также должна заменять 'berries' на 'berry'.

Ингредиенты и их себестоимость:

Strawberries $1.50
Banana $0.50
Mango $2.50
Blueberries $1.00
Raspberries $1.00
Apples $1.75
Pineapple $3.50


Примеры вызовов:

s1 = Beverage(["Banana"])
s1.ingredients ➞ ["Banana"]
s1.get_cost() ➞ "$0.50"
s1.get_price() ➞ "$1.25"
s1.get_name() ➞ "Banana Smoothie"

s2 = Beverage(["Raspberries", "Strawberries", "Blueberries"])
s2.ingredients ➞ ["Raspberries", "Strawberries", "Blueberries"]
s2.get_cost() ➞ "$3.50"
s2.get_price() ➞ "$8.75"
s2.get_name() ➞ "Blueberry Raspberry Strawberry Fusion"""


class Beverage:
    COAST = {'Strawberries': 1.50,

             'Banana': 0.50,

             'Mango': 2.50,

             'Blueberries': 1.00,

             'Raspberries': 1.00,

             'Apples': 1.75,

             'Pineapple': 3.50}

    def __init__(self, ingredients):

        self.ingredients = ingredients

    def get_cost(self):

        s = 0

        for i in self.ingredients:
            s += Beverage.COAST[i.capitalize()]

        return f'${s}'

    def get_price(self):

        s = 0

        for i in self.ingredients:
            s += Beverage.COAST[i.capitalize()]

        return f'${s * 2}'

    def get_name(self):

        for i in range(len(self.ingredients)):

            if self.ingredients[i] == 'berries':
                self.ingredients[i] = 'berry'

        if len(self.ingredients) < 2:

            return ' '.join(self.ingredients) + ' Smoothie'

        else:

            return ' '.join(self.ingredients) + ' Fusion'
