from collections import deque
from pprint import pprint

# =================================
# Deque FIFO -> First In, First Out
# =================================

# Двусторонняя очередь deque() поддерживает поточно-ориентированные,
# эффективные по памяти операции добавления и извлечения элементов последовательности
# с любой стороны с примерно одинаковой производительностью O(1) в любом направлении

print("\n---Пример дека")
ex = list("python")
deque_ex = deque(ex)
print(f"{ex = }")
print(f"{deque_ex = }")
print(deque_ex.__class__.__mro__)

print("\n---Добавление элементов в дек ПО ОДНОМУ")
print(f"{deque_ex = }")
deque_ex.append('E')      # добавление в конец
deque_ex.appendleft('A')  # добавление в начало (левый конец)
print(f"{deque_ex = }")

print("\n---Извлечение элементов из дека")
print(f"{deque_ex = }")
right_elem = deque_ex.pop()
left_elem = deque_ex.popleft()
print(f"{deque_ex = }")
print(f'Извлеченный слева элемент: {left_elem}')
print(f'Извлеченный справа элемент: {right_elem}')

print("\n---Добавление элементов в дек СПИСКОМ")
print(f"{deque_ex = }")
deque_ex.extend([10, 11])
deque_ex.extendleft([98, 99]) # [99, 98, 'p', ...]
print(f"{deque_ex = }")

print("\n---Подсчет элементов в деке")
print(f"{deque_ex = }")
print(f"{deque_ex.count('p') = }")
print(f"{deque_ex[3] = }")
print(f"{len(deque_ex) = }")

print("\n---Перенос 3 элементов из конца дека в начало")
print(f"{deque_ex = }")
deque_ex.rotate(3)
print(f"{deque_ex = }")

print("\n---Перенос 3 элементов из начала дека в конец")
print(f"{deque_ex = }")
deque_ex.rotate(-3)
print(f"{deque_ex = }")

print("\n---Преобразование дека в список")
print(f"{deque_ex = }")
lst = list(deque_ex)
print(f"{lst = }", type(lst))

print("\n---Использование дека при работе с файлом")

# Параметр maxlen определяет количество элементов в очереди
def tail(filename, n=10):
    """ Возвращает n последних строк файла """
    with open(filename) as f:
        return deque(f, maxlen=n)


print(*tail('zen.txt'), sep='')
