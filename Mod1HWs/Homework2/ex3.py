# Вводим координаты клетки от 1 до 8
x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))

# Складываем координаты
sum = x + y

# Проверяем четность суммы
if sum % 2 == 0:
    # Если сумма четная, клетка белая
    print("YES")
else:
    # Если сумма нечетная, клетка черная
    print("NO")