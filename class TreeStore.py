"""
ЗАДАНИЕ
Есть массив объектов, которые имеют поля id и parent, через которые их можно связать в дерево и некоторые произвольные поля.

Нужно написать класс, который принимает в конструктор массив этих объектов и реализует 4 метода:
#  - getAll() Должен возвращать изначальный массив элементов.
#  - getItem(id) Принимает id элемента и возвращает сам объект элемента;
#  - getChildren(id) Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента,
# чей id получен в аргументе. Если у элемента нет дочерних, то должен возвращаться пустой массив;
#  - getAllParents(id) Принимает id элемента и возвращает массив из цепочки родительских элементов,
# начиная от самого элемента, чей id был передан в аргументе и до корневого элемента,
# т.е. должен получиться путь элемента наверх дерева через цепочку родителей к корню дерева. Порядок элементов важен!

Требования: максимальное быстродействие, следовательно, минимальное количество обходов массива при операциях,
# в идеале, прямой доступ к элементам без поиска их в массиве.
#
"""


class TreeStore:
    def __init__(self, items: list):
        self.items = items

    def getAll(self) -> list:
        return self.items

    def getItem(self, id: int) -> dict:
        # Для задачи с отсортированными по id данными идущими подряд без пропусков достаточно будет self.items[id]
        return [item for item in self.items if item["id"] == id][0]

    def getChildren(self, id: int) -> list:
        return [item for item in self.items if item["parent"] == id]

    def getAllParents(self, id: int) -> list:
        children_item = self.getItem(id)
        all_parents = []
        while children_item["parent"] != "root":
            for item in self.items:
                if item["id"] == children_item["parent"]:
                    all_parents.append(item)
                    children_item = item
                    break
        return all_parents


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)
