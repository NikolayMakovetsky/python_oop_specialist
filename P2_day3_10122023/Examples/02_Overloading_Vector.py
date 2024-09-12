# =============================
#    Перегрузка операторов
# =============================
from __future__ import annotations
from pprint import pprint


# Имена методов, начинающиеся и заканчивающиеся двумя символами
# подчеркивания __X__, имеют специальное назначение.
# Такие методы вызываются неявно, когда объект участвует в соответствующей операции.
# Возвращаемое значение метода становится результатом соответствующей операции.


class Vector:
    def __init__(self, pos: list | tuple):  # list или tuple
        self.x = pos[0]
        self.y = pos[1]

    # При вызове v1+v2 отработает v1.__add__(v2)
    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x, self.y + other.y))

    # def __radd__(self, other: Vector) -> Vector:
    #     return Vector((self.x + other.x, self.y + other.y))

    # Этот явный метод каждый раз будет возращать новый экземпляр
    def add(self, other: Vector) -> Vector:
        return Vector((self.x + other.x, self.y + other.y))

     # Это явный метод
    def as_point(self) -> tuple:
        return self.x, self.y

    def __str__(self):
        return f"Vector(x:{self.x}, y:{self.y})"

    def __repr__(self):
        return f"Vector(x:{self.x}, y:{self.y})"


print("\n---Создаем экземпляры класса (объекты)")
v1 = Vector((10, 15))
v2 = Vector((12, 10))

print("\n---Явно вызываем явный метод")
print(v1.add(v2))

print("\n---Наши объекты участвуют в операции сложения (+)")
v3 = v1 + v2       # v1.__add__(v2)
print('v3 =', v3)  # v3.__str__()

print("\n---На самом деле это работает так:")
v4 = v1.__add__(v2)
print(f'{v4 = !s}')
# v4 = v1 - v2  # TypeError: unsupported operand type(s) for -: 'Vector'

# =========
# Проясняем
# =========
print("\n---Можно ли сложить Вектор со Слоном?---")

class Slon:
    def __init__(self):
        self.x = 100.0
        self.y = 200.0

slonik = Slon()
something = v1 + slonik  # v1.__add__(slonik)  work
# some_v2 = slonik + v2  # slonik.__add__(v2)  error
# print(some_v2, type(some_v2))
# ВАЖНО. Если бы у Vector'a был реализован метод __radd__() то этот код отработал бы.

print("\n---Функция print() для получения строки для вывода вызывает методы __str__()")
print('v3 + v3 =', v3 + v3)
print('Repr of v3 = ', repr(v3))
print(f'{v3!r}')  # __repr__()
print(f'{v3!s}')  # __str__()
