
# Определяем функцию с именем max_number, которая принимает два или три аргумента: a, b и c
# Для третьего аргумента указываем значение по умолчанию None, чтобы он был необязательным
def max_number(a, b, c=None):
    # Если c равно None, то сравниваем только a и b
    if c == None:
        # Если a больше или равно b, то возвращаем a
        if a >= b:
            return a
        # Иначе возвращаем b
        else:
            return b
    # Иначе сравниваем все три числа
    else:
        # Если a больше или равно b и a больше или равно c, то возвращаем a
        if a >= b and a >= c:
            return a
        # Если b больше или равно a и b больше или равно c, то возвращаем b
        elif b >= a and b >= c:
            return b
        # Иначе возвращаем c
        else:
            return c

# Примеры вызова функции с разными аргументами
print(max_number(1, 2)) # 2
print(max_number(3, 2, 4)) # 4
print(max_number(5, 5, 5)) # 5