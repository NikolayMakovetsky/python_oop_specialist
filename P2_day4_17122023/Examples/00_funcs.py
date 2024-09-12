# Функция полноправный объект в языке Python:
# • может быть создан во время выполнения;
# • может быть присвоен переменной или полю структуры данных;
# • может быть передан функции в качестве аргумента;
# • может быть возвращен функцией в качестве результата.

from collections.abc import Callable
from pprint import pprint


# функция для примеров
def func(text: str) -> str:
    return text.upper() + '!'

print("\n---Тестируем нашу функцию func")
print(type(func), id(func))
print(func('привет'))

print("\n---Создаем еще одну ссылку на func и записываем ее в переменную bar")
bar = func
print(type(bar), id(bar))
print(bar('пока'))

print("\n---Объект (в т.ч. функция) существует пока есть ссылки на него")
del func
# print(func('textest'))  # Out -> Error
print(bar('Я все еще работаю'))
print(bar.__name__)
print(type(bar), id(bar))

print("\n---Можно хранить функции в структурах данных")
funcs = [bar, str.lower, str.capitalize]
pprint(funcs)

print("\n---Доступ к функциям, хранящимся внутри списка")
for function in funcs:
    print(function.__name__, '->', function('проверка Работы'))

print("\n---Вызов функции как элемента списка по индексу")
print(funcs[0]('первая функция'))

print("\n---Словарь функций")
d = {'first': str.upper
     ,'second': bar
     ,'third': str.capitalize
     }

print(d['first']('hello'))  # str.upper('hello')
print(d['second']('arg'))
print(d['third']('foo'))


print("\n---Передача функции в качестве аргумента в другую функцию")
def greet(fun: Callable) -> None:
    greeting = fun('Программа на Python')
    print(greeting)


print("\n--Вызов функции greet с аргументом - функцией bar")
greet(bar)                      # Out: ПРОГРАММА НА PYTHON!
# greet('hello')                # Error т.е. передается строка, а не функция
print(callable(bar))            # True т.к. есть реализация __call__()
print(callable('hello'))        # False
print(bar.__call__("hello"))    # эквивалент bar('hello')
print(callable(int))            # True


print("\n---Вторая функция для примера")
def imp_func(text: str) -> str:
    return text.lower() + '. Done!'


print("\n---Вызов функции greet с аргументом - функцией imp_func")
greet(imp_func)

# Полезные модули. Ссылка на документацию
# https://docs.python.org/3/library/itertools.html
# https://docs.python.org/3/library/functools.html
# https://more-itertools.readthedocs.io/en/stable/api.html

