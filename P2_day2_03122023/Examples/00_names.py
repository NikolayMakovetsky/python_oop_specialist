from pprint import pprint # Красивый вывод словаря(вертикально)


class People:
    """ class for learning """
    name = "Teachers"


print("---дандер метод __name__")
print(People.__name__) # Встроенный(системный)
People.__name__ = 'Some people'
print(People.__name__)

print("---Cоздаем атрибут name в классе")
print(f"{People.name = }")
print(f"{id(People) = }")
p = People()            # создаю экземпляр на основе класса People
print(f"{p.name = }")   # атрибут берется из класса, если он в экземпляре не переопределен
P1 = People             # еще одна ссылка на класс People
person1 = P1()          # создаю экземпляр на основе класса People
print(f"{id(P1) = }")

print(id(People) == id(P1))     # True
print(People is P1)             # True

print(p)  # repr(p)
print(f'{hex(id(p)).upper(): >45}') # отступ 45 сделать (форматирование строки)
