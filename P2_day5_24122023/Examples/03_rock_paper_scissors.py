""" Реализация игры "Камень, ножницы, бумага" """
import random


class Thing(object):
    def __str__(self):
        return f'{self.__class__.__name__}'


class Rock(Thing):
    pass


class BrownRock(Rock):
    pass


class Paper(Thing):
    pass


class WhitePaper(Paper):
    pass


class Scissors(Thing):
    pass

# isinstance(object, classinfo)
# object          объект, требующий проверки
# classinfo       класс,
#                 кортеж с классами,
#                 рекурсивный кортеж кортежей,
#                 несколько классов: int | str (с версии Python 3.10)
# Функция isinstance() вернет True,
# если проверяемый объект object является экземпляром
# любого указанного в classinfo класса (классов)
# или его подкласса (прямого, косвенного или виртуального)

def beats(x, y):
    if isinstance(x, Rock):
        if isinstance(y, Rock):
            return None  # Нет победителя
        elif isinstance(y, Paper):
            return y
        elif isinstance(y, Scissors):
            return x
        else:
            raise TypeError("Unknown second thing")
    elif isinstance(x, Paper):
        if isinstance(y, Rock):
            return x
        elif isinstance(y, Paper):
            return None  # Нет победителя
        elif isinstance(y, Scissors):
            return y
        else:
            raise TypeError("Unknown second thing")
    elif isinstance(x, Scissors):
        if isinstance(y, Rock):
            return y
        elif isinstance(y, Paper):
            return x
        elif isinstance(y, Scissors):
            return None  # Нет победителя
        else:
            raise TypeError("Unknown second thing")
    else:
        raise TypeError("Unknown first thing")


b_rock, w_paper, scissors = BrownRock(), WhitePaper(), Scissors()
lst = [b_rock, w_paper, scissors, Rock(), Paper()]

for _ in range(10):
    first = random.choice(lst)
    second = random.choice(lst)
    print(f'{first} vs {second}. {beats(first, second)} win')


# beats(w_paper, 3)  # TypeError: Unknown second thing

print("\n---Примеры работы функций type и isinstance")
print(type(w_paper) is Paper)       # False
print(type(w_paper) is WhitePaper)  # True
print(isinstance(w_paper, Paper))   # True
print(isinstance(b_rock, Thing))    # True
print(isinstance(True, int))        # True

print("\n---MRO - демонстрация иерархии классов") 
print(b_rock.__class__.__mro__)
print(True.__class__.__mro__)

print("\n---Примеры работы функции issubclass")
print(issubclass(BrownRock, Thing))  # True
print(issubclass(Rock, object))      # True
print(issubclass(Rock, Scissors))    # False

# аргументы - только классы, поэтому ошибка
# print(issubclass(b_rock, Thing))  # Error

