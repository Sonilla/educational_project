"""Создать класс Pagination, который обрабатывает некое содержимое постранично. Пагинация используется для того,
чтобы делить длинные списки на как-бы на страницы.

Конструктор принимает два параметра:
items (по умолчанию: []): - список строкового содержимого, который мы будем пагинировать
page_size (по умолчанию: 10): кол-во экземпляров строк, показываемых на одной странице

Класс реализует функцию get_visible_items возвращающую элементы на текущей странице.

Класс также должен предоставлять набор функций для перемещения по страницам:

prev_page # переход на предыдущую страницу
next_page # переход на следующую страницу
first_page # переход на первую страницу
last_page # переход на последнюю страницу
go_to_page # принимает номер страницы в качестве аргумента, осуществляет переход на конкретную страницу
           # если передано число > числа страниц, то перейти на последнюю, если < 1 то перейти на первую

Также, класс должен поддерживать следующие функции:

get_current_page возвращающая текущий номер страницы
get_page_size возвращающая размер страницы
get_items возвращающая список строк

Например, мы можем создать наш класс следующим образом:

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
А затем вызвать get_visible_items чтобы вывести содержимое текущей страницы (текущая страница - первая)

p.get_visible_items() ➞ ["a", "b", "c", "d"]
Если перейти на следующую страницу и снова вызвать get_visible_items, то получим ["e", "f", "g", "h"]

p.next_page() p.get_visible_items() ➞ ["e", "f", "g", "h"] На последней странице должно быть всего два элемента,
так что если вызвать last_page и get_visible_items, то получим ["y", "z"]

p.last_page()
p.get_visible_items() ➞ ["y", "z"]
Заметки:

Аргумент page_size и аргумент функции go_to_page передаются только типом int, не надо защищаться от float.

Функции перемещения по страницам должны быть реализованы таким образом, чтобы их можно было вызывать цепочкой:
p.next_page().next_page().prev_page()p.last_page().prev_page()p.first_page().next_page()p.go_to_page(10).next_page()"""


class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            items = []
        self.items = {0: []}
        p = 0
        for item in items:
            if len(self.items[p]) == page_size:
                p += 1
                self.items[p] = []
            self.items[p].append(item)
        self.page_size = page_size
        self.page = 0

    # возвращает элементы на текущей странице.
    def get_visible_items(self):
        return self.items[self.page]

    # переход на предыдущую страницу
    def prev_page(self):
        self.page -= 1
        return self

    # переход на следующую страницу
    def next_page(self):
        self.page += 1
        return self

    # переход на первую страницу
    def first_page(self):
        self.page = 0
        return self

    # переход на последнюю страницу
    def last_page(self):
        self.page = len(self.items) - 1
        return self

    # принимает номер страницы в качестве аргумента, осуществляет переход на конкретную страницу
    # если передано число > числа страниц, то перейти на последнюю, если < 1 то перейти на первую
    def go_to_page(self, page_number):
        self.page = int(page_number)
        return self

    # возвращающая текущий номер страницы
    def get_current_page(self):
        return self.page + 1

    # возвращающая размер страницы
    def get_page_size(self):
        return len(self.items[self.page])

    # возвращающая список строк
    def get_items(self):
        return self.items
