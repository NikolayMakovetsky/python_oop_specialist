class Point:
    version = 1

    # Конструктор класса
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


print("---Создаем объекты класса с помощью конструктора")
point1 = Point(10, -8)
point2 = Point(12, 5)
point3 = Point(y=5)  # point3 = Point(0, 5)

print("---")
print("point1.x =", point1.x)
print("point1.y =", point1.y)
print("point1.version =", point1.version)

print("---")
print("point2.x = ", point2.x)
print("point2.y = ", point2.y)
print("point2.version =", point2.version)

print("---")
print("point3.x = ", point3.x)
print("point3.y = ", point3.y)
print("point3.version =", point3.version)

print("---Используя конструктор, мы не создаем атрибуты в родетильском классе")
# ERROR
# AttributeError: type object 'Point' has no attribute 'x'
# print(Point.x)
print(hasattr(Point, 'x'))  # Out: False
print(hasattr(point1, 'x')) # Out: True
print(hasattr(point1, 'version'))  # Out: True

print("---Создадим атрибут x для класса")
Point.x = 12
print(Point.x)  # Out: 12
print(point3.x)  # Out: 0 т.к. экземпляр ищет значение атрибута сначала у себя, а потом в классе
print(f'{point3.version = }')

# Используем значения по умолчанию
point4 = Point()        # point4 = Point(0, 0)
point5 = Point(x=10)    # point5 = Point(10, 0)

print("---")
print("point4.x =", point4.x)
print("point4.y =", point4.y)
print("point4.version =", point1.version)

print("---")
print("point5.x =", point5.x)
print("point5.y =", point5.y)
print("point5.version =", point5.version)

point4.x = 999
print(point4.x)  # Out: 999


print("Экземпляр динамически обновляет информацию из класса")
Point.z = 12     # Добавили новый атрибут в класс
print(point1.z)  # Out: 12
print(point2.z)  # Out: 12
print(point3.z)  # Out: 12
print(point4.z)  # Out: 12
print(point5.z)  # Out: 12

print("Создаем значение атрибута только для point1.z")
point1.z = 78
print(point1.z)  # Out: 78
print(point2.z)  # Out: 12
print(point3.z)  # Out: 12
print(point4.z)  # Out: 12
print(point5.z)  # Out: 12

print("Удаляем атрибут только для point1.z")
del point1.z
print("after del point1.z:")
print(point1.z)  # Out: 12
print(point2.z)  # Out: 12
print(point3.z)  # Out: 12
print(point4.z)  # Out: 12
print(point5.z)  # Out: 12

print("Что будет если удалить атрибут экземпляра")
print(point1.y)
del point1.y
# print(point1.y)  # Error
# del point1.w     # Error
