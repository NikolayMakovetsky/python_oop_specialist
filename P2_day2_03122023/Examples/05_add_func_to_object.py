import pprint as pp


class MyClass:
    def __init__(self, n):
        self.name = n


# Создаем экземпляры класса
A = MyClass('A')
B = MyClass('B')


# Создаем функцию с аргументом
def hello(self):
    print("Этo экземпляр", self.name, "респечатанный функцией hello")


# Создаем функцию с аргументом
def hi(some_obj):
    print("Объект", some_obj.name, "респечатан функцией hi")


# hello('value') # Ошибка, потому что у строки нет атрибута name
print("\n---Работа функции hello вне класса")
hello(A)

print("\n---Добавляем функцию в класс через атрибут say")
MyClass.say = hello
print(MyClass.say)
pp.pprint(MyClass.__dict__)

print("\n---Вызываем методы экземпляров")
A.say() 
B.say()

print("\n---Вызываем функцию класса")
MyClass.say(A)  # A.say()
MyClass.say(B)  # B.say()

print("\n---Перенаправляем атрибут-ссылку say на функцию hi вместо hello")
MyClass.say = hi

print("\n---Вызываем методы экземпляров")
A.say()
B.say()
print(A.say, type(A.say))
print(B.say, type(B.say))


print("\n---Вызываем функцию класса")
MyClass.say(A)  # A.say()
MyClass.say(B)  # B.say()



print("\n---Теперь мы создаем атрибут у экземпляра A")
print('Before:', vars(A))   # Out V1: {'name': 'A'}
A.say = hello
print('After:', vars(A))

print("\n---Используем функцию hello через экземпляр")
# Обязательно передаем аргумент, потому что
# работа идет не через класс МуClass
A.say(A) # A.say()  # Error
B.say()  # MyClass.say(B) работает через класс,
         # т.к. для экземпляра B атрибут say не определен
pp.pprint(MyClass.__dict__)
pp.pprint(A.__dict__)
pp.pprint(B.__dict__)

print("\n---Здесь класс MyClass не используем")
A.say(B)   # Out: B - hello

print("\n---А здесь класс MyClass используем")
# B.say(A)   # Out: Error

print("\n---Удаляем функцию класса")
del MyClass.say
print("After del:")
print(vars(A))
print(vars(B))
pp.pprint(vars(MyClass))

print("\n---Вызываем функцию экземпляра")
A.say(A)
# B.say()  # AttributeError: 'MyClass' object has no attribute 'say'


print("\n--- КАК ПИСАТЬ НЕ СЛЕДУЕТ ---")

class Person:
    def __init__(some, name):
        some.name = name
        print(id(some))

    def add(self, s: str):
        self.name += s
        print(f'{self.name = }')
        print(id(self))
        result = self.third()
        print(f'{result = }')

    def second(abcd):
        abcd.name += ' work'
        print(f'{abcd.name = }')
        print(id(abcd))

    def third(work):
        print(id(work))
        return work.name[:3]


p = Person('Петр')
print(id(p))
print('Before:', p.name)
p.add('!!!')  # Person.add(p)  s = '!!!'
print('After:', p.name)
p.second()   # Person.second(p)

