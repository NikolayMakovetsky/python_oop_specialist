# =============================
#    Перегрузка операторов
# =============================

# Имена методов, начинающиеся и заканчивающиеся двумя символами
# подчеркивания __X__, имеют специальное назначение.
# dunder(magic) methods.
# Такие методы вызываются неявно, когда объект участвует в соответствующей операции.
# Возвращаемое значение метода становится результатом соответствующей операции.
from pprint import pprint


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # это явный метод
    def to_str(self):
        return f'Point({self.x},{self.y})'

    # Перегрузка(переопределение) магического(dunder) метода:

    def __repr__(self) -> str:  # repr()
        return f'Point({self.x},{self.y})'

    def __str__(self) -> str:  # str()
        return f'Точка с координатами(x={self.x},y={self.y})'


# =====================
# Примеры для str, repr
# =====================

print("\n---Пример разницы str и repr при работе со строкой и числом")

print(str('C:\name'))   # выводит переменную
print('C:\name'.__str__())

print("---")
print(repr('C:\name'))  # выводит переменную 'как есть'
print('C:\name'.__repr__())

print("---")
print(r'C:\name')       # raw string


print("\n---Функция len() воспринимает '\\n' как один символ! ")
print('\not'.__len__())
# print(len(i1))  # AttributeError: 'int' object has no attribute '__len__'

print("\n---Создали два экземпяра")
p1 = Point(3, 3)
p2 = Point(4, 4)

print("\n---Явно вызываем метод to_str()")
print(p1.to_str())
print(p2.to_str())

print("\n---Вызов неявных методов")
print(p1)
print(p2)

print("\n---Неявно вызываем магические методы __repr__ и __str__")
# print сначала ищет __str__(), если не находит то использует __repr__()
print(str(p1))  # str(p1) -> p1.__str__()
print(repr(p2))  # repr(p1) -> p2.__repr__()


print("\n---Четыре вызова с одинаковым функционалом")
print(p2)
print(str(p2))
print(p2.__str__())
print(Point.__str__(p2))


print("\n---Вызваем именно repr()")
print(p1.__repr__())
print(repr(p1))

print("\n---Интроспекция экземпляра p1 (dunder методы)")
pprint(dir(p1))
print(p1.__sizeof__())
# help(p1.__sizeof__)   # вывести на экран описание функции __sizeof__()

print("\n---Полезные функции модуля sys")
import sys

print("\n---Размер объекта в байтах")
print(sys.getsizeof(p1))
# help(sys.getsizeof)

print("\n---Количество ссылок на объект")
print(sys.getrefcount(p1))
print(sys.getrefcount(Point))
print(sys.getrefcount(5))
print(sys.getrefcount(-5))
print(sys.getrefcount(256))


print("\n---Создадим функцию для интроспекции")
def func(a=5, b=8):
    return a + b

print("\n---Интроспекция экземпляра func (dunder методы)")
pprint(dir(func))
pprint(func.__defaults__)           # вывести значения по-умолчанию
pprint(func.__code__.co_argcount)   # вывести кол-во аргументов
pprint(func.__code__.co_varnames)   # вывести имена аргументов

print("\n---Интроспекция при помощи модуля inspect")
import inspect as ins

pprint(func.__code__)                   # вывести местонахождение функции
print(ins.getsource(func.__code__))     # вывести код самой функции
print(type(func))                       # вывести тип объекта

print("\n---Добавляем атрибут к нашей функции func")
func.name_of_function = 'first function'  # work
print(func.name_of_function)

print("\n---К встроенной функции добавить собственный атрибут нельзя")
# sum.name_of_function = 'sum function'    # error
