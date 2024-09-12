# Функции более высокого порядка(higher-order functions)
# map, filter, reduce

from collections.abc import Callable
from pprint import pprint


# функция для примеров
def func(text: str) -> str:
    return text.upper() + '!'

bar = func

# ===
# map
# ===

# print("\n---Применение функции bar к списку строк")
# print(map(bar, ['hello', 'hi', 'привет']))
# print(set(map(bar, ['hello', 'hi', 'привет'])))

# print("\n---Преобразование в список вводимых с клавиатуры чисел")
# numbers = list(map(int, input("Enter: ").split()))
# print(numbers)
# numbers = [int(value) for value in input("Enter: ").split()]
# print(numbers)

# print("\n---Применение функции bar к вводимым данным и запись в кортеж")
# strings = tuple(map(bar, input("Enter: ").split(maxsplit=2)))
# # Параметр maxsplit определяет максимальное количество разделений
# # Значение по умолчанию -1 (будут выполнены все разделения)
# print(strings)


print("\n---Здесь действует распаковка")
a = map(float, "23 44 67".split())
print(f'{a = }')
print(next(a))  # a.__next__()
print(next(a))  # a.__next__()
print(next(a))  # a.__next__()
print(next(a, "I'm empty."))

print("\n---Распаковка двух чисел с преобразованием")
a, b = map(float, "23 7".split())
print(f'{a = }, {b = }')

print("\n---Оператор * позволяет сразу выводить объект на печать")
print(*map(int, '4 8'.split()))

print("\n---Просуммируем символы в списке строк")
print(sum(map(len, ['hello', 'hi', 'привет'])))

