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

# # ==========================================
# #   Объект живет, пока есть ссылка на него
# # ==========================================

del People # p2 = People()  # Out: NameError: name 'People' is not defined
del P1

print("---Воссоздание ссылки People через объект p")

print(vars(p))      # Получаем словарь объекта
People = type(p)    # Создаем снова имя(ссылку) People

pprint(vars(People)) # Получаем словарь объекта

print("\n---Создание экземпляра используя другой экземпляр и его ссылку на класс")
new_p = type(p)()           # new_p = People()
print(new_p, type(new_p))


print("\n---Создание экземпляра, используя дандер-метод __class__ другого экземпляра")
p2 = p.__class__()  # p2 = People()
print(p2, type(p2))


print("---Доступ к имени класса через экземпляр")
# Получаю доступ к классу экземпляра и затем к имени класса
p = People()
print(p.__class__.__name__)     # Out: People
print(People.__name__)          # Out: People

# # Но здесь ошибка!
# # print(p.__name__)  # AttributeError
print("---Пользовательский класс наследуется от класса 'type'")
print(type(People))  # <class 'type'>


# ===========================
# # Доступ к полям класса.
# # Получаем словарь объекта
# ===========================
# p = People()
# pprint(People.__dict__)  # vars(People)
# People.count = 20
# print(p.count)
# print(p.name)
# pprint(People.__dict__)
# pprint(p.__dict__)  # Out: {}
#
# # Создаем значение для атрибута экземпляра
# p.count = 30
# pprint(p.__dict__)
# pprint(p.__class__.__dict__)  # People.__dict__
# print(p.count)
# print(p.__class__.count)    # People.count
# print(vars(p).get('name'))  # None
# print(vars(p).get('count'))  # 30
#
# # # Проверка наличия атрибута у экземпляра
# print(hasattr(p, 'name'))  # p.name
#
# del People.name
# pprint(People.__dict__)
# # print(p.name)  # AttributeError
# del People.count
# pprint(People.__dict__)
# print(p.count)  # Ошибки не будет
#
# p.name = 'Students'
# p.age = 22
# pprint(p.__dict__)
#
# # функция vars покажет словарь атрибутов объекта
# print(vars(p))
# pprint(vars(People))

# Меняем значение атрибута класса через экземпляр
# p = People()
# p.__class__.name = 'SName'  # People.name = 'SName'
# pprint(People.__dict__)
# print(p.__dict__)




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

