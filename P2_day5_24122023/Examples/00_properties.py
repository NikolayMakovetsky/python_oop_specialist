print("\n---Удобная работа с атрибутами класса")
print("\n---Встроенный декоратор property(): getter, setter, deleter")
# Такой способ позволяет запретить пользователю обращаться напрямую к атрибутам

class StudentA:
    """ Test class for learning """
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('From get_name()')
        return self._name

    def set_name(self, value):
        print('From set_name()')
        self._name = value

    def del_name(self):
        print('From del_name()')
        self._name = ''

    # Есть 3 способа, как можно задать getter, setter, deleter:
    # V1
    # Для чтения(getter) -> get_name, для изменения(setter) -> set_name, для удаления(deleter) -> del_name
    # name = property(fget=get_name, fset=set_name, fdel=del_name)
    # For example: print(student.name); student.name = 12; del student.name

    # V2
    # name = property()
    # print(type(name))
    # print(dir(name))
    # name = name.getter(get_name)
    # name = name.setter(set_name)
    # name = name.deleter(del_name)

    # V3
    # Первый аргумент - это getter(считать значение)
    name = property(get_name)
    name = name.setter(set_name)
    name = name.deleter(del_name)

print("\n---getter work")
student = StudentA('first')
print(student.__dict__)
print(student.name)        # fget=get_name

print("\n---setter work")
student.name = 'second'  # fset=set_name
print(student.name)
print(student.__dict__)

print("\n---deleter work")
del student.name        # fdel=del_name
print(student.__dict__)
print(repr(student.name)) # print(student.name) тоже можно

print("\n---setter work 2")
student.name = 'third'
print(student.__dict__)
print(student.name)  # Считываем значение _name с помощью getter'а
print(student._name) # Считываем значение _name напрямую?
print(type(student.name))


print("\n---Обычно property используют как декоратор")
class StudentB:
    ''' Test class for learning '''
    def __init__(self, name):
        self._name = name

    # name = property(name)
    @property
    def name(self):
        return self._name

    # name = name.setter(set_name)
    # мы должны явно указать имя аттрибута, для которого указываем setter
    @name.setter
    def name(self, value):
        if len(value) > 3:
            self._name = value
        else:
            raise Exception('Too short')

    # name = name.deleter(del_name)
    # мы должны явно указать имя аттрибута, для которого указываем deleter
    @name.deleter
    def name(self):
        self._name = ''


print("\n---Результат работы getter'а")
s_b = StudentB('Петр')
print(s_b.__dict__)
print(s_b.name, type(s_b.name))
# print(s_b.name())   # TypeError: 'str' object is not callable

print("\n---Результат работы setter'а")
s_b.name = 'Вася'
print(s_b.__dict__)
print(s_b.name)

print("\n---Результат работы deleter'а")
del s_b.name
print(s_b.__dict__)
print(f'{s_b.name!r}')


print("\n---В setter есть проверка данных")
# s_b.name = 'Ник'  # error Exception: Too short
