from pprint import pprint # Красивый вывод словаря(вертикально)

# =============
# Методы класса
# =============

class Student:
    def __init__(self, name='Ivan'):
        self.name = name
        self.surname = 'Kozlov'

    def hello1(self) -> None:
        self.name += ' Pertovich'

    def hello2():
        print('Hello, Student')        

    def hello3(self) -> None:
        print(self.name, self.surname)



print("\n---Печать ФУНКЦИИ класса (методы у экземпляров!)")
print(f'{id(Student) = }')
print(Student.hello1)
print(f'{hex(id(Student.hello1)).upper() = }')

print("\n---Создаем экземпляр sb")
sb = Student()


print("\n---id не совпадают. Почему?")
print(f'{id(sb) = }')
print(sb.hello1)                            # id не совпадают. Почему?
print(f'{hex(id(sb.hello1)).upper() = }')   # id не совпадают. Почему?


print("\n---Работаем через класс")
sb.hello1()             # Student.hello1(sb)
print(sb.name)          # Ivan Pertovich
Student.hello1(sb)      # sb.hello1()
print(sb.name)          # Ivan Pertovich Pertovich # Повторный вызов функции добавил слово

print("\n---Вызов метода через класс, либо через экземпляр")
sb.hello3()
Student.hello3(sb)  # sb.hello3()

print("\n---Важный момент с hello2()")
Student.hello2()      # Отработает
# sb.hello2()         # TypeError, т.к. в hello2 не прописано слово self
# Student.hello2(sb)  # TypeError, т.к. в hello2 не прописано слово self

print("\n---Структура экземпляра. здесь id СОВПАДАЮТ! Почему?")
print(sb.__dict__)
print(sb.hello1.__self__)       # здесь id СОВПАДАЮТ! Почему?
print(hex(id(sb)).upper())      # здесь id СОВПАДАЮТ! Почему?

# print(sb.__self__)  # AttributeError: 'Student' object has no attribute '__self__'
print(sb.hello1.__func__)
print(type(sb.hello1))
print(type(sb.name))

