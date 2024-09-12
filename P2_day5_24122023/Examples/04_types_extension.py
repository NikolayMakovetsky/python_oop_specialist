# ================================
#   Расширение встроенных типов
# ================================

# Функция super() в Python позволяет наследовать базовые классы
# (они же суперклассы или родительские классы)
# без необходимости явно ссылаться на базовый класс.
# Обычно метод super() используется в методе __init__

print("\n---Расширяем стандартный class dict")

class MyDict(dict):
    # Добавляем свой метод
    def new_method(self):
        return "Вызвали new_method()"

    # Добавляем дополнительный функционал к существующему методу __setitem__
    # который запускается при использовании конструкции d[key] = value
    def __setitem__(self, key, value):
        print(f'Setting {key!r} to {value!s}')
        key = str(key).upper()
        value = 'INSERTION + ' + str(value)
        # Создаем объект родительского класса
        # С помощью super() начинаем поиск атрибутов(поля и методы) с класса предка / предков
        return super().__setitem__(key, value)

print("\n---Создаем обычный словарь")
d = dict(((5, 23), (6, 12)))
print(d)
print(d.items())

print("\n---Создаем наш словарь MyDict")
m_dict = MyDict(((3, 23), (89, 12)))
print(m_dict)
print(m_dict.items())

print("\n---Неявно вызываем для m_dict метод __setitem__ выполняя присваивание")
m_dict["new_key"] = "new_value"     # __setitem__
m_dict[4] = 12                      # __setitem__

print(m_dict)
print(f"{m_dict['NEW_KEY'] = }")
print(m_dict.keys())
print(m_dict.new_method())


print("\n---Fortran(fortran translator) расширяем стандартный класс list")
class FList(list):
    offset = 1 # смещение
    """ Список, индексы которого начинаются с 1, а не с 0
        __getitem__(5) -> lst[5]  """
    def __getitem__(self, index):
        print(f'indexing at {index}', end=': ')

        if index - self.offset < 0:
            raise IndexError('Index must be positive!')

        return list.__getitem__(self, index - self.offset)


print("\n---Создаем список типа (класса) FList")
x = FList('1234567890ABCDEF')   # __init__ наследуется из списка
print(x)                        # __repr__ наследуется из списка

print("\n---Убедимся, что новая индексация работает в соответствии с задумкой")
# print(x[0])   # IndexError
print(x[1])     # MyList.__getitem__
print(x[5])     # Изменяет поведение метода суперкласса
print(x[16])

print("\n---Используем методы, унаследованные от суперкласса list")
x.append('spam')
print(x)

x.reverse()
print(x)

x[4] = 999  # __setitem__(4) это пятый элемент в list !!! (мы его еще не перегружали)
print(x)  
print(x[4]) # __getitem__ -> D
print(x[5]) # __getitem__ -> 999

