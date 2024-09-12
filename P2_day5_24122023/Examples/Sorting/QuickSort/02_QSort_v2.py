# Быстрая сортировка quicksort

# Cортируем так:
# Берем нулевой элемент
# Далее формируем два списка:
# - список с элементами, которые меньше или равны взятому элементу
# - cписок с элементами, которые больше взятого элемента
# Для каждого из полученных списков рекуксивно запускаем эту же функцию,
# а наш нулевой элемент вставляем посередине



def qsort(x):
      if len(x) < 2:  # Базовый случай
          print('Base case =>', x)
          return x
      else:
          pivot = x[0]
          print(f'{pivot = }')
          less = [i for i in x[1:] if i <= pivot]
          print(f'{less = }')
          greater = [i for i in x[1:] if i > pivot]
          print(f'{greater = }')
          return qsort(less) + [pivot] + qsort(greater)


array = [54, 1, 2, 3, 52, 3, 1, 2, 3, 5, 3, 67, 3, 2, 543]
print(f"{array = }")
print(qsort(array))
