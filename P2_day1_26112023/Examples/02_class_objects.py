class Point:
    # Поля(fieds) == атрибуты класса
    x = 7
    y = 4


# Создадим несколько объектов-точек
# Экземпляр(instance)
point1 = Point()
point2 = Point()

print("---Работа с атрибутом x")
# Считываем атрибуты
print(point1.x)  # 7
print(point2.x)  # 7

point1.x = 10
print(point1.x)  # 10 берется из класса
print(point2.x)  # 7 берется из класса

Point.x = -15
print(point1.x)  # 10 т.к. это значение присвоено в экземпляре класса
print(point2.x)  # -15 т.к. по прежнему берется из класса

print("---Создание нового атрибута z")
Point.z = 999
print(point1.z)  # 999
print(point2.z)  # 999

point2.z = -99
print(point1.z)  # 999
print(point2.z)  # -99 т.к. значение берется в первую очередь у экземпляра класса
                 # а если такового не находится, то берется из родительского класса 

# Удаляем у экземпляра
del point2.z
print(point1.z)  # 999
print(point2.z)  # 999

# Удаляем у класса
del Point.z
# print(point1.z)   # Out: AttributeError:
# print(point2.z)   # Out: AttributeError:

# del point1
# print(point1.x)  # Out: NameError

print("---Создание собственных атрибутов для экземпляров")
point1.name = 'first instance'
print(point1.name)
print(point1)
print("                              ", hex(id(point1)).upper())

# del point1.y     # Out: AttributeError:
