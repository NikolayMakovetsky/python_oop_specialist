# Функции более высокого порядка(higher-order functions)
# map, filter, reduce

from collections.abc import Callable
from pprint import pprint


def condition(text):
    return len(text) > 3

# ======
# filter
# ======

print("\n---Включаем элемент в итоговый список, если результат работы condition = True")
print(list(filter(condition, ['hello', 'hi', 'привет'])))

print("\n---Если первый аргумент None, то в итог попадут только truthy values")
print(tuple(filter(None, [True, 5, 0, '', 8.2, 'hello', False])))
