from collections.abc import Callable
from pprint import pprint

# ==================
# Области видимости
# Local -> Enclosed -> Global -> Builtin (LEGB)
# ==================

print("\n---Вложенные функции")
a = 1
print(f"{a = }")

def main(text: str):
    global a    # Режим, устанавливающий в этой области видимости
                # работу с переменной а как с глобальной
                # Две переменных а (одна глобальная, другая локальная) быть не может
    a = 2       # Присваиваем глобальной а новое значение
    b = 100
    print(f"{a = }, {b = }")

    def inner(in_text: str) -> str:
        nonlocal b  # Переменную b берем из внешней области видимости
        b = 101     # Присваем внешней переменной b новое значение
        print(f"INNER: {locals() = }")     # Словарь локальных переменных
        return in_text.lower() + ' | [inner function return] | ' + f'{a = }, ' + f'{b = }'
    
    print(f"MAIN: {locals() = }")         # Словарь локальных переменных
    return inner(text)              # ВЫЗОВ ВНУТРЕННЕЙ ФУНКЦИИ

print(main('Привет'))   # Выполняет свой код, потом код внутренней функции, а после
                        # возвращает результат внутренней функции

# print(inner_func('Любая фраза'))      # Error
# print(main.inner_func)                # Error


print("\n---Функция возвращающая другую функцию, в зависимости от переданного аргумента")
def main_imp(size: int):
    def foo(text):
        return text.lower() + '.' * size

    def bar(text):
        return text.upper() + '!' * size

    if size > 5:
        return foo
    return bar


print(main_imp(3))  # out-> function main_imp.<locals>.bar
print(main_imp(7))  # out-> function main_imp.<locals>.foo
some_name = main_imp(1)
print(some_name, type(some_name))
print(some_name('привет'))

print("\n---Вызываем сразу две функции подряд")
print(main_imp(10)('Test'))     # foo("Test")
print(main_imp(3)('Student'))   # bar('Student')

print("\n---Используем область видимости Enclosed")
def main_imp_2(size: int, text='default'):
    # Вложенным функциям доступны локальные
    # переменные родительской функции из
    # области видимости Enclosed
    def foo():
        return text.lower() + '.' * size

    def bar():
        return text.upper() + '!' * size

    if size > 5:
        return foo
    return bar

print(main_imp_2(10, 'TEST')())     # foo() т.к. 10 > 5
print(main_imp_2(3)())              # bar() т.к. 3 < 5

