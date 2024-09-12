# 4 типа наследуемых классов:
# * Класс-наследник    | Полностью повторяет структуру класса-предка (pass)
# * Класс-поставщик    | Реализует функции, которые существуют, но не реализованы в классе-предке
# * Класс-расширитель  | Расширяет функционал методов класса-предка
# * Класс-заместитель  | Полностью меняет реализацию функции класса-предка


# Класс Предок (Супер-класс)
class Super:
    # Стандартное поведение
    def method(self):
        print('in Super.method')

    def delegate(self):
        print('START delegate method')
        self.action()
        print('FINISH delegate method')

    # Ожидается перегрузка(переопределение) метода
    def first(self):
        assert False, 'first must be defined'


# Буквальное наследование всех методов из Super
class Inheritor(Super): # Класс-наследник
    pass


# Заполнение обязательного метода в Provider.action
class Provider(Super): # Класс-поставщик
    def action(self):
        print('in Provider.action')


# Полное замещение метода в Replacer.method (добавить Provider)
class Replacer(Provider, Super): # Класс-заместитель
    def method(self):
        print('in Replacer.method')

    def first(self):
        print('method <first> in Replace defined')


# Расширение поведения метода
class Extender(Super): # Класс-расширитель
    def method(self):
        # начало Extender.method
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')
        # конец Extender.method


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print(klass)  # class or instance? Классы vs Экземпляры
        print('\n' + klass.__name__ + '...')
        # Inheritor().method(), Replacer().method(), Extender().method()
        klass().method()
        print('=' * 40)

    print('\n---Provider (Поставщик)')
    p = Provider()
    p.delegate()  # двойная пробежка !!!

    print('\n---Inheritor (Наследник)')
    i = Inheritor()
    # i.first()  # AssertionError: first must be defined
    print('done')

    print('\n---Replacer (Заместитель)')
    r = Replacer()
    r.first()

    print('\n---Extender (Расширитель)')
    e = Extender()
    # e.first()  # AssertionError: first must be defined
    e.method()
    
    print("\n---MRO - method resolution order (Порядок обхода классов при поиске атрибутов и методов)")
    r = Replacer()
    print(r.__class__.__mro__)
