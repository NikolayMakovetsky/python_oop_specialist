print("\n---Запуская функцию в питоне можно изменить передаваемый в нее объект")
def func(lst: list):  # lst = lst
    lst.append('W')
    return s

s = list('hello')
print(f"{s = }")
func(s)
print(f"{s = }")

print("\n---Работа механизма share memory (разделение памяти)")
def func_two(lst: list):  # lst = lst
    lst = lst[:] # добавляем эту строчку, чтобы далее работать с копией объекта
    lst.append('W')
    return s

s = list('hello')
print(f"{s = }")
func_two(s)
print(f"{s = }")


print("\n---Вариант ошибки если мы не используем разделение памяти")
def func_three(lst: list = [], number=100):
    """При запуске без аргументов хотим, чтобы возвращала [100]"""
    # разделение памяти мы не используем
    lst.append(number)
    return lst


gl_lst = [4, 8, 10]
print(f'{id(gl_lst) = }')
result = func_three(gl_lst)
print(result)

result2 = func_three()
print(result2)  # [100] 

result3 = func_three()
print(result3)  # [100, 100] (вместо одной сотни они постепенно множатся)

result4 = func_three()
print(result4)  # [100, 100, 100] (вместо одной сотни они постепенно множатся)


print("\n---Работа механизма share memory (разделение памяти)")
def good_func(lst=None, number=100):
    if lst is None:
        lst = []
    lst.append(number)
    return lst


gl_lst = [4, 8, 10]
print(f'{id(gl_lst) = }')
result = good_func(gl_lst)
print(result)

result2 = good_func()
print(result2)  # [100]

result3 = good_func()
print(result3)  # [100]

result4 = good_func()
print(result4)  # [100]
