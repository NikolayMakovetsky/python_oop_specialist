from pprint import pprint # Красивый вывод словаря(вертикально)


class People:
    """ class for learning """
    name = "Teachers"


P1 = People
p = People()
psn = P1()

print(P1.__name__)  # People
print(p.name)       # Teachers
print(psn.name)     # Teachers


# ===========================
# # Доступ к полям класса.
# # Получаем словарь объекта
# ===========================

p = People()
pprint(People.__dict__)     # vars(People)

print("\n---Создаем атрибут класса")
People.count = 20           # создали еще один атрибут класса
print(p.count)              # 20
print(p.name)               # Teachers (берется из класса)
pprint(People.__dict__)     # новый атрибут 'count' тоже отображается
pprint(p.__dict__)          # Out: {}


print("\n---Создаем атрибут экземпляра")
p.count = 30
pprint(p.__dict__)              # {'count': 30}
pprint(p.__class__.__dict__)    # People.__dict__
print(p.count)                  # 30

print(p.__class__.count)        # People.count = 20
print(vars(p).get('name'))      # None
print(vars(p).get('count'))     # 30


print("\n---Проверка наличия атрибута у экземпляра")
print(hasattr(p, 'name'))  # True

del People.name             # удаляем атрибут класса
pprint(People.__dict__)
# print(p.name)  # AttributeError
del People.count            # удаляем атрибут класса
pprint(People.__dict__)
print(p.count)  # 30 # Ошибки не будет, т.к. у экземпляра свой атрибут count

print("\n---Создаем атрибуты 'name', 'age' для экземпляра")
p.name = 'Students'
p.age = 22
pprint(p.__dict__)

print(vars(p))      # функция vars покажет словарь атрибутов объекта
pprint(vars(People))

print("\n---Меняем значение атрибута класса через экземпляр")
p = People()
p.__class__.name = 'SName'  # People.name = 'SName'
pprint(People.__dict__)
print(p.__dict__)



# ==========================================
# Функции getattr, setattr, delattr, hasattr
# ==========================================
# value = 'name'
# # имя объекта, имя атрибута,
# print(getattr(People, value))  # Out: People.name -> SName
#
# # Вернет третий аргумент, если атрибута нет
# print(getattr(People, 'name2', 'Такого нет'))
# # print(People.name2)   # AttributeError
#
# # Шаблон вызова: название класса, имя атрибута, значение атрибута
# field_name = 'course'
# setattr(People, field_name, 'Python')  # People.course = 'Python'
# pprint(People.__dict__)
#
#
# # Пример использования функции setattr
# from string import ascii_letters as chars
# from random import choice
# new_field = choice(chars)
# print(f'{new_field = }')
# setattr(People, new_field, 1)
# pprint(vars(People))
# print(getattr(p, new_field))
#
# # ## Удаляем атрибут
# delattr(People, 'course')
# pprint(People.__dict__)


# p.age = 22
# pprint(vars(p))
# # проверка наличия атрибута у объекта(класс, экземпляр)
# print(hasattr(People, 'age'), hasattr(People, 'name'))
# print(hasattr(p, "name"), hasattr(p, 'age'))
# print(p.name)
#
#
# # Проверка понимания
# People.some = 567
# # Это не только проверка словаря экземпляра, но и класса
# print(hasattr(p, 'some'))  # Вспомнить и проверить
# print(p.some)
# print(vars(p).get("some"))
# print(getattr(p, 'some'))  #

# =============
# Методы класса
# =============
# class Student:
#     def __init__(self, name='Ivan'):
#         self.name = name
#         self.surname = 'Ivanov'
#
#     def hello1(self) -> None:
#         self.name += ' Ivanovich'
#
#     def hello3(self) -> None:
#         print(self.name, self.surname)
#
#     def hello2():
#         print('Hello, Student')
#
#
# print(f'{id(Student) = }')
# print(Student.hello1)
# print(id(Student.hello1))
# sb = Student()
# print(f'{id(sb) = }')
# print(sb.hello1)
# print(id(sb.hello1))
#
# # Работаем через класс
# sb.hello1()  # Student.hello1(sb)
# # print(sb.name)
# # Student.hello1(sb)  # sb.hello1()
# # print(sb.name)
#
# # ## Два одинаковых вызова
# sb.hello3()
# Student.hello3(sb)  # sb.hello3()
#
# # Важный момент с hello2()
# Student.hello2()      # Отработает
# # sb.hello2()         # TypeError
# # Student.hello2(sb)  # TypeError
# #
# print(sb.__dict__)
# print(sb.hello1.__self__)
# print(hex(id(sb)).upper())
#
# # print(sb.__self__)  # AttributeError
# print(hex(id(sb)))
# print(sb.hello1.__func__)
# print(type(sb.hello1))
# print(type(sb.name))

