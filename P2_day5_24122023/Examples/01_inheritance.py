
# Наследование подразумевает,
# что дочерний класс содержит все атрибуты родительского класса,
# при этом некоторые из них могут быть перегружены(переопределены)
# или добавлены в дочернем.


print("\n---Рассмотрим классы Student и Teacher")
class Student:
    def __init__(self, name: str, surname: str, birth_date: str, school, class_room: str):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.school = school
        self._class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}

    @property
    def class_room(self):
        return f"{self._class_room['class_num']} {self._class_room['class_char']}"

    def next_class(self):
        self._class_room['class_num'] += 1

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name


class Teacher:
    def __init__(self, name, surname, birth_date, school, teach_classes):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.school = school
        self.teach_classes = list(map(self.convert_class, teach_classes))
        # Список строк преобразуется в список словарей

    def convert_class(self, class_room):
        """
        '<class_num> <class_int>' --> {'class_num': <class_num>, 'class_int': <class_int>}
        """
        return {'class_num': int(class_room.split()[0]),
                'class_char': class_room.split()[1]}

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name

print("\n---student")
student1 = Student('Ivan', 'Petrov', '01.01.1990', 111, "1 A")
print(student1.name)            # Ivan
print(student1.class_room)      # 1 A
student1.next_class()           # 2 A
print(student1.class_room)      # {'class_num': 2, 'class_char': 'A'}
print(student1._class_room)     # ??

print("\n---teacher")
teacher = Teacher('Petr', 'Ivanov', '01.01.1991', 111, ["1 A", '2 B'])
print(teacher.teach_classes)    # [{'class_num': 1, 'class_char': 'A'}, {'class_num': 2, 'class_char': 'B'}]
print(teacher.name)             # Petr

print(""" ------------------------------
# Классы Student и Teacher описывают два различных объекта
# Но часть информации у них общая(атрибуты, методы)
# Общую информацию выносим в Класс-предок (родитель)
------------------------------""")
print("\n---Рассмотрим класс Person")

class Person(object):
    def __init__(self, name, surname, birth_date, school):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.school = school

    @property
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name


# =========================
print("\n---Класс SchoolPerson наследуем Person 'как есть'")
class SchoolPerson(Person):
    pass

st = SchoolPerson('Petr', "Ivanov", "11.22.2023", '1515')
print(type(st))             # <class '__main__.SchoolPerson'>
print(st.name)              # Petr
print(st.surname)           # Ivanov
print(st.get_full_name)     # Petr Ivanov
st.set_name("Ivan")
print(st.get_full_name)     # Ivan Ivanov
# =========================


print("\n---Классы Student и Teacher наследуем от Person")

class Student(Person):
    def __init__(self, name, surname, birth_date, school, class_room):
        # Явно вызываем конструктор родительского класса
        Person.__init__(self, name, surname, birth_date, school)
        # Добавляем уникальные атрибуты
        self._class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}

    # И уникальные методы
    @property
    def class_room(self):
        return f"{self._class_room['class_num']} {self._class_room['class_char']}"

    def next_class(self):
        self._class_room['class_num'] += 1


class Teacher(Person):
    def __init__(self, name, surname, birth_date, school, teach_classes):
        # Явно вызываем конструктор родительского класса
        Person.__init__(self, name, surname, birth_date, school)
        # Уникальный атрибут Учителя
        self.teach_classes = list(map(self.convert_class, teach_classes))

    # Уникальный метод Учителя
    def convert_class(self, class_room):
        """
        '<class_num> <class_int>' --> {'class_num': <class_num>, 'class_int': <class_int>}
        """
        return {'class_num': int(class_room.split()[0]),
                'class_char': class_room.split()[1]}

print(""" ----------------------
Наследование позволяет избежать дублирования кода
и повторно использовать уже готовые реализации
----------------------""")

print("\n---student")
student1 = Student('Ivan', 'Petrov', '01.01.1990', 111, "1 A")
print(student1.class_room)          # 1 A
print(student1.get_full_name)       # Ivan Petrov
student1.set_name('Alexey')
print(student1.name)                # Alexey
print(student1.surname)             # Petrov
print(student1.birth_date)          # 01.01.1990
print(student1.school)              # 111
print(student1.get_full_name)       # Alexey Petrov
student1.next_class()
print(student1.class_room)          # 2 A

print("\n---teacher")
teacher1 = Teacher('Petr', 'Ivanov', '05.05.1990', 111, ["1 A", "2 A", "3 A"])
print(teacher1.name)                    # Petr
print(teacher1.get_full_name)           # Petr Ivanov
print(teacher1.teach_classes)           # [{'class_num': 1, 'class_char': 'A'},
                                        # {'class_num': 2, 'class_char': 'A'},
                                        # {'class_num': 3, 'class_char': 'A'}]
print(teacher1.convert_class("2 A"))
teacher1.set_name('Nikolay')            
print(teacher1.name)                    # Nikolay
print(teacher1.get_full_name)           # Nikolay Ivanov
print(teacher1.surname)                 # Ivanov
print(teacher1.birth_date)              # 05.05.1990
print(teacher1.school)                  # 111
