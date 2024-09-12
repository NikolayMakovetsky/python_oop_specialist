from collections.abc import Callable
from pprint import pprint

# ==================
# Lambda functions
# ==================
# Lambda-функция возвращает только одно значение


print("\n---x + y")
add = lambda x, y: x + y
print(add(2, 3), type(add))
print(add)

print("\n---Вызов лямбды с аргументами")
print((lambda x, y: x + y)(10, 16))
print((lambda x, y: (x, y))(10, 16)) # помещаем аргументы в кортеж

print("\n---Можно, но не нужно")
print((lambda *args, **kwargs: (args, kwargs))(4, 5, b='hello', c='hi'))
print((lambda *args, **kwargs: (args, kwargs))(41, 51))

print("\n---Пример функции с произвольным количеством аргументов (*args, **kwargs)")
# args - это кортеж позиционных аргументов
# kwargs - это словарь именованных аргументов
def func_1(*args, **kwargs):
    print(args, kwargs)


print("\n---Замыкание с использованием lambda в качестве вложенной функции")
def multiply(num1):
    return lambda num2: num1 * num2

print(multiply(10)(20))     # 10*20=200

print("\n---lambda в качестве значения аргумента key")

list_of_tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
print(list_of_tuples, "без сортировки")
# sorted принимает как аргумент последовательность и всегда возвращает список
print(sorted(list_of_tuples), "сортировка по цифрам")

def new_order(x):
    return x[1]

print(sorted(list_of_tuples, key=lambda x: x[1]), "сортировка по буквам")
print(sorted(list_of_tuples, key=new_order), "сортировка по буквам")
# Out: [(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]

print("\n---Примеры сортировок по ключу с использованием lambda")
# 0 1 1 4 4 9 9 16 16 25 25 - ключ(критерий) сортировки
print(sorted(range(-5, 6), key=lambda x: x * x))
print(sorted(range(5, -6, -1), key=lambda x: x * x))
print(sorted('hello', key=lambda x: ord(x) % 10))

print("\n---Пример с заменой символов в строке")
In = "hel545 py5n st495 hel55 hel54 py5n"
result = set(map(lambda x: x.replace('5', '*').replace('4', '*'), In.split()))
print(len(result))  # Кол-во элементов? Вспомнить всё и проверить
print(result)


print("\n---Пример использования lambda с min и max")

s = 'hello python java go golang'
print(min(s.split(), key=len))                              # go
print(min(s.split(), key=lambda x: x.count('o')))           # java
print(max(s.split(), key=lambda x: x.count('o')))           # hello
print(max(s.split(), key=lambda x: x.count('h')))           # hello
print(min(s.split(), key=lambda x: x.count('n') + len(x)))  # go
print(min(range(20), key=lambda x: x % 3))                  # 0
print(max(range(20), key=lambda x: x % 3))                  # 2
print(min(range(13, 20), key=lambda x: x % 3))              # 15

