# Функция полноправный объект в языке Python:
# • может быть создан во время выполнения;
# • может быть присвоен переменной или полю структуры данных;
# • может быть передан функции в качестве аргумента;
# • может быть возвращен функцией в качестве результата.


# ==========
# Декораторы
# ==========


def null_decorator(func):
    return func


def greet(): # greet = здороваться
    return 'Привет!'


print("\n---Механизм работы декоратора")
print("Before:")
print(greet())
greet = null_decorator(greet)  # сам механизм
print("After:")
print(greet())


print("\n---Функция-декоратор")
def uppercase(func):
    def wrapper(): # обертка
        original_result = func()
        modified_result = "<{[" + original_result.upper() + "]}>"
        return modified_result
    return wrapper


print("\n---Декоратор")
@uppercase  # тоже самое, что и greet_eng = uppercase(greet_eng)
def greet_eng() -> str:
    return 'Hello!'

print(greet_eng())  # out -> <<<<HELLO!>>>>
print(greet_eng)


print("\n---Для сохранения базовой функции создаем новую переменную")
greet_eng_new = uppercase(greet_eng)
print(greet_eng_new())      # В данном случае мы обернули два раза
print(greet_eng())

greet_rus_new = uppercase(greet)
print(greet_rus_new())


print("\n---Универсальная функция-декоратор (*args, **kwargs)")
def other(func):
    # Кладем все аргументы декорируемой функции в функцию wrapper
    def wrapper(*args, **kwargs):
        print(f'{args = }')
        print(f'{kwargs = }')
        original_result = func(*args, **kwargs)
        modified_result = original_result * 1.5
        return modified_result
    return wrapper



print("\n---Переопределяем встроенную функцию sum")
print(sum((100, 100), start=1000))  # 1200
sum = other(sum)                    # применили декоратор
print(sum((100, 100), start=1000))  # 1800 !
print(sum)

print("\n---Применение нескольких декораторов")
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper


def emphasis(func): # акцент
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper


print("\n---Порядок применения снизу вверх")
@strong    # Второй по порядку
@emphasis  # Первый по порядку
def greet2():
    return 'Привет!'

print(greet2())

print("\n---Применение двух декораторов без синтаксического сахара")
greet2 = strong(emphasis(greet2))
print(greet2())
print(greet2)

# В Python трассировка - это отчет, содержащий вызовы функций,
# выполненные в вашем коде в определенный момент.
# Благодаря трассировке в коде можно найти ошибку,
# отслеживая выполнение функций в обратном направлении (traceback)

print("\n---Функция-трассировщик написанная с использованием декоратора")
def trace(func):
    def wrapper(*args, **kwargs):
        print(f"Трассировка функции {func.__name__}(); {args = }; {kwargs = }")
        original_result = func(*args, **kwargs)
        print(f"Трассировка функции {func.__name__}() вернула: {original_result!r}")
        return f"Результат работы: {original_result}"
    return wrapper


@trace
def say(name, line):
    return f'{name * 3}: {line} as is'


print(say('hi', line='Hello'))
print("---")
print(say('hello', 5.2))
print("---")
print(say(line=10, name='user'))


