from collections.abc import Callable
from pprint import pprint

# =========
# Замыкания
# =========
# Замыкание (англ. closure) в программировании — функция первого класса,
# в теле которой присутствуют ссылки на переменные, объявленные вне тела
# этой функции в окружающем коде и не являющиеся её параметрами.
# Говоря другим языком, замыкание — функция, которая ссылается на
# свободные переменные в своей области видимости.

def multiply(num1: int): # функция-замыкание

    # локальная переменная var удалится после вызова функции multiply
    var = 1
    num1 += var

    # Вложенная функция
    def inner(num2: int):
        return num1 * num2
    return inner

print("\n---Создаем собственные функции используя аргумент num1")
mult_by_9 = multiply(9)     # т.к. num1 += var mult_by_9 умножает на 10
mult_by_10 = multiply(10)   # т.к. num1 += var mult_by_10 умножает на 11

print("\n---Это разные объекты")
print(f"{id(mult_by_9) = }")
print(f"{id(mult_by_10) = }")
print(mult_by_9)  # Out: <function __main__.multiply.<locals>.inner(num2)>
print(mult_by_9.__closure__)  # Out: (<cell at 0xb0bd5f2c: int object at 0x836bf60>,)
print(mult_by_9.__closure__[0].cell_contents)   # Out: 10
print(mult_by_10.__closure__[0].cell_contents)  # Out: 11
print([c.cell_contents for c in mult_by_9.__closure__])  # Out: 10

print("\n---Вызываем функцию inner с аргументом num2")
print(mult_by_9(10))  # Out: 100
print(mult_by_9(2))   # Out: 20
print(mult_by_10(4))  # Out: 44
print(mult_by_10(5))  # Out: 55

print("\n---Используем замыкание напрямую !!!")
print(multiply(9)(10))  # Out: 100
print(multiply(9)(2))   # Out: 20
print(multiply(10)(4))  # Out: 44
print(multiply(10)(5))  # Out: 55

print(mult_by_9.__code__.co_argcount)   # Количество аргументов inner
print(mult_by_9.__code__.co_freevars)   # Свободные переменные ('num1',)
print(mult_by_9.__code__.co_name)       # co = code object

print("\n---Исходный код функции")
import inspect as ins

print(ins.getsource(mult_by_9.__code__))

