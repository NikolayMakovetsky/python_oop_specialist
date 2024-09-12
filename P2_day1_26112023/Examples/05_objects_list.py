class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


points = [Point(10, -8), Point(12, 5)]

print("---Выведем координату x первой точки")
print(points[0].x)

print("---Выведем координату y второй точки")
print(points[1].y)

print("---Механизм работы списка не меняется")
lst = [str(456), float('890.23'), int('6'), set('890')]
print(lst[0], lst[1], lst[2].denominator, lst[3], sep=" | ") # denominator = знаменатель
print(lst[2].as_integer_ratio())  # Out: (6, 1) # ratio = соотношение
print(lst[0][1:], type(lst[0][1:])) # срез строки
