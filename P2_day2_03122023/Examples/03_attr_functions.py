from pprint import pprint # Красивый вывод словаря(вертикально)


class People:
    """ class for learning """
    name = "Teachers"


P1 = People
p = People()
psn = P1()


# ==========================================
# Функции getattr, setattr, delattr, hasattr
# ==========================================

print("\n---getattr")
# getattr (имя объекта, имя атрибута, аргумент возвращаемый если атрибута нет)
# берет атрибут из экземпляра ИЛИ ИЗ ВЫШЕСТОЯЩЕГО КЛАССА !!! и возвращает его

p = People()
p.__class__.name = 'SName'
value = 'name'
print(getattr(People, value))  # Out: People.name -> SName
print(getattr(People, 'name2', 'Такого нет'))
# print(People.name2)   # AttributeError

print("\n---setattr")
# setattr (название класса, имя атрибута, значение атрибута)
field_name = 'course'
setattr(People, field_name, 'Python')  # People.course = 'Python'
pprint(People.__dict__)

print("\n---Пример использования функции setattr")
from string import ascii_letters as chars
from random import choice

new_field = choice(chars)       # присваиваем new_field случайный английский символ
print(f'{new_field = }')
setattr(People, new_field, 1)   # создаем атрибут с именем хранящимся в new_field

pprint(vars(People))
print(getattr(p, new_field))


print("\n---delattr")
# delattr (название класса, имя атрибута)
delattr(People, 'course')
pprint(People.__dict__)


print("\n---hasattr")
p.age = 22
# hasattr (объект: класс или экземпляр, название атрибута)
# hasattr ПРОВЕРЯЕТ НЕ ТОЛЬКО СЛОВАРЬ ЭКЗЕМПЛЯРА, НО И КЛАССА (СМОТРИТ ВСЮ ЦЕПОЧКУ)
print(hasattr(People, 'age'), hasattr(People, 'name'))
print(hasattr(p, "name"), hasattr(p, 'age'))
print(p.name)   # SName
print(p.age)    # 22

print("\n---Проверка понимания")
People.some = 567
print(hasattr(p, 'some'))   # True
print(p.some)               # 567
print(vars(p).get('some'))  # None т.к. в словаре экземпляра атрибут не содержится
print(getattr(p, 'some'))   # 567 т.к. берет атрибут из класса




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

