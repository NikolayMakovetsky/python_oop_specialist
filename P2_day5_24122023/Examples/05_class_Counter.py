from collections import Counter
from pprint import pprint

# Метод setdefault() возвращает значение ключа (если ключ находится в словаре)
# Если такого ключа нет, он вставляет ключ со значением по умолчанию в словарь.

print("\n---Счетчик из обычного словаря")
d_usual = dict()
print(type(d_usual))

for word in ['spam', 'egg', 'egg', 'spam',
             'counter', 'counter', 'counter']:

    d_usual.setdefault(word, 0) # вставка нового ключа в словарь d_usual (value = 0)
                                # если ключ существует - вставки не происходит
    d_usual[word] += 1          # СЧЕТЧИК СЛОВА увеличиваем на 1


# print(d_usual['col'])   # Error: KeyError
print(d_usual.get("col", 0))
print(d_usual.get("spam", 0))
print(d_usual.get("egg", 0))
print(d_usual.get("counter", 0))

print(d_usual)


# =============
# класс Counter
# =============

print("\n---Та же задача, реализованная с помощью класса Counter")
counter = Counter()
print(type(counter))

for word in ['spam', 'egg', 'egg', 'spam',
             'counter', 'counter', 'counter']:
    counter[word] += 1    # Нет ошибки(в обычном dict будет)

print(counter)
print(counter.__class__.__mro__) # <class 'collections.Counter'> сделан на базе <class 'dict'>
print(counter['col'])  # Нет ошибки
print(counter['spam'])
print(counter['egg'])
print(counter['counter'])


print("\n---Пример создания на лету")
print(Counter('count_symbols_in_string'))

print("\n---Вернуть 3 самых часто встречающихся элемента")
print(Counter('hello students, language python'))
print(Counter('hello students, language python').most_common(3))


print("\n---Вернуть 2 самых редко встречающихся элемента")
print(Counter('hello students, language python'))
print(Counter('hello students, language python').most_common()[:-3:-1]) # [('y', 1), ('p', 1)]
print(Counter('hello students, language python').most_common()[-2:])    # [('p', 1), ('y', 1)]

print("\n---ОПЕРАЦИИ НАД СЧЕТЧИКАМИ Counter")
c1 = Counter(a=4, b=2, c=0, d=-2)
c2 = Counter(a=1, b=2, c=3, d=4)
print(f"{c1 = }")
print(f"{c2 = }")

print("\n---Остаются только ключи с положительными значениями (c1+c2) (c1-c2)")
print('Сложение c1+c2:\n', c1+c2)
print('Вычитание c1-c2:\n', c1-c2)  # Counter({'a': 3}) часть ключей удалилось


print("\n---Остаются только ключи с минимальными значениями, строго > 0 (c1 & c2)")
print(f"{c1 = }")
print(f"{c2 = }")
print('Минимальные значения:', c1 & c2)

print("\n---Остаются только ключи с максимальными значениями, строго > 0 (c1 | c2)")
print(f"{c1 = }")
print(f"{c2 = }")
print('Максимальные значения:', c1 | c2)

print("\n---Остаются ключи со всеми значениями (+, 0, -) (c1.subtract(c2))")
print(f"{c1 = }")
print(f"{c2 = }")
c1.subtract(c2)
print(c1)

print("\n---Положит.значения +c1 и Отриц.значения -c1")
print(c1)
print(f'{+c1 = }')     # пары с положительными значениями
print(f'{-c1 = }')     # пары с неположительными значениями
print(list(c1))        # list(counter.keys())

print("\n---Возврат всех элементов c1 (нулевые и отрицательные игнорируются)")
print(f"{c1 = }")
print(list(c1.elements()))  # Counter({'a': 3}) -> 'a', 'a', 'a'
print(''.join(c1.elements()))

print("\n---Возврат всех элементов res")
res = Counter('count_symbols_in_string')
print(f'{res = }')
print(''.join(res.elements()))  # Здесь ошибки нет

print("\n---Общая сумма по значениям")
print(f"{c1 = }")
print(sum(c1.values()))

print("\n---Вызов явного метода total()")
print(f"{c1 = }")
print(c1.total())

print("\n---удалить элементы, встречающиеся менее одного раза")
print(f"{c1 = }")
c1 += Counter()
print(f"{c1 = }")


print("\n---Подсчет слов в файле")
"""
Как создать файл
cmd.exe
chcp 65001
py -c "import this" > zen.txt
powershell:
py -c "import this" | out-file zen.txt -encoding utf8
"""
import re # модуль для работы с регулярными выражениями Regular Expressions

# https://regex101.com/  [а-яА-ЯёЁ]
# \w+ - буквы, цифры и _, длина от 1 и более

words = re.findall(r'[\w\']+', open('zen.txt', encoding="utf8").read().lower())
print(type(words))

zen_dict = Counter(words)
pprint(zen_dict)
print(f"Всего {zen_dict.total()} слова")

