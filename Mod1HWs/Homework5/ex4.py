# Вводим три строки
s1 = input()
s2 = input()
s3 = input()
# Разбиваем строки по пробелам и преобразуем в множества
s1 = set(s1.split())
s2 = set(s2.split())
s3 = set(s3.split())
# Находим пересечение множеств
s = s1 & s2 & s3
# Если пересечение не пусто
if s:
    # Сортируем его в алфавитном порядке и выводим через пробел
    print(*sorted(s))
# Иначе
else:
    # Выводим сообщение, что все три задачи никто не решил
    print("Все три задачи никто не решил")