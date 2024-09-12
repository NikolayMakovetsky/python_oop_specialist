def add(n):
    if n == 1:
        print(f'Базовый случай {n = }')
        return n
    else:
        print(f'{n = }')
        return n + add(n - 1)


print(add(5))
