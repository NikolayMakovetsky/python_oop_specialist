print("---------Работа ссылочной модели Питона---------")

print("---Числа от -5 до 256 в Питоне уже созданы и исп-ся для внутр работы!!!")
a = -5
b = -5
print(a == b)  # Out: True
print(a is b)  # Out: True (True даже при построчном запуске через терминал)

c = 256
d = 256
print(c == d)  # Out: True
print(c is d)  # Out: True (True даже при построчном запуске через терминал)

print("---Работа с числами за пределами диапазона [-5, 256]----")
# мы не видим разницы, т.к. код исполняется в рамках одного запуска интерпретатора
# REPL - read evaluate print loop
# при работе с питоном через терминал каждая команда будет обрабатываться отдельно
# и мы увидим, что a = -6, b = -6, c = 257, d = 257 это 4 разных объекта
a = -6
b = -6
print(a == b)  # Out: True
print(a is b)  # Out: True (False при построчном запуске через терминал)

c = 257
d = 257
print(c == d)  # Out: True
print(c is d)  # Out: True (False при построчном запуске через терминал)

print("---Работа со строками без спецсимволов")
# пробел это тоже спецсимвол
s1 = 'hello'
s2 = 'hello'
print(s1 == s2)  # Out: True
print(s1 is s2)  # Out: True (True даже при построчном запуске через терминал)

print("---Работа со строками содержащими спецсимволы")
# пробел это тоже спецсимвол
s1 = 'hello$%^'
s2 = 'hello$%^'
print(s1 == s2)  # Out: True
print(s1 is s2)  # Out: True (False при построчном запуске через терминал)

print("---Работа со списками")
lst1 = [45, 3]
lst2 = lst1[:]       # lst2.copy() тоже самое
print(lst1 == lst2)  # True
print(lst1 is lst2)  # False (полный срез и метод copy() возвращают новый список)

lst1 = [45, 3]
lst2 = lst1          # две ссылки на один список
lst2.append(100)     # lst1.append(100) тоже самое
print(lst1 == lst2)  # True
print(lst1 is lst2)  # True
lst1.pop()
print(lst1, lst2)

print("---Работа кортежем (unmutable type)")
tup1 = ([45], 3)
tup1[0].append(100)     # внутрь неизменяемого кортежа можно поместить изменяемый элемент
print(f'{tup1 = }')
# tup1[0] = 1           # Error (сам элемент кортежа изменять нельзя)
# dict_example = {tup1: 12}  # TypeError: unhashable type: 'list'
                             # we cannot use lists as keys in dicts or elements in sets
                             # and in this case we have list inside tuple
tup2 = tup1[:]          # полный срез кортежа, в отличие от списка, дает тот же кортеж
print(tup1 == tup2)     # True
print(tup1 is tup2)     # True

print("---Контрольный вопрос")
s3 = 'hello!@Ж'
s4 = s3[:]        # s4 = s3
print(s3 == s4)   # True
print(s3 is s4)   # True


