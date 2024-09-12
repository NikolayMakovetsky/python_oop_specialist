from collections.abc import Callable
from pprint import pprint

# ======
#  zip 
# ======

print("\n---Объединяем элементы с одинаковым индексом")
a = tuple(range(10))
b = list(range(11, 17))
c = list(range(101, 120))
d = 'hello python'
pprint(list(zip(a, b, c, d)))


print("\n---Объединяем строку и последовательность")
for zip_item in zip('pythonpy', range(8)):
    print(zip_item)

print("\n---Пример на понимание работы словаря")

d1 = dict((('a', 2), ('b', 9)))
print(f'{d1 = }')

d = dict(zip('pythonpy', range(8))) # элементов получилось 6, т.к. ключи уникальные
print(f'{d = }')
print(f"{len(d) = }")               # 6

