
# Вводим две строки
s1 = input()
s2 = input()
# Удаляем пробелы из строк
s1 = s1.replace(" ", "")
s2 = s2.replace(" ", "")
# Преобразуем строки в множества
s1 = set(s1)
s2 = set(s2)
# Сравниваем множества
if s1 == s2:
    # Выводим сообщение, что строки являются анаграммами
    print("Строки являются анаграммами")
else:
    # Выводим сообщение, что строки не являются анаграммами
    print("Строки не являются анаграммами")