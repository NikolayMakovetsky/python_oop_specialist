# Функции более высокого порядка(higher-order functions)
# map, filter, reduce

from collections.abc import Callable
from pprint import pprint
from functools import reduce


def add_two(a, b):
    print('Привет из функции add_two')
    print(f'{a = }')
    print(f'{b = }')
    print('Функция отработала')
    print('=' * 40)
    return a + b


# ======
# reduce "сокращение"
# ======

print(reduce(add_two, ['hello', 'hi', 'привет'], 'START:'))

