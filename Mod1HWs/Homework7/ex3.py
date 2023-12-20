# Импортируем модуль functools, который содержит функцию reduce
import functools

# Задаем список
list = [19, 65, 57, 39, 152, 190, 20, 85, 68, 143]

# Используем reduce и lambda для вычисления наибольшего элемента в списке
result = functools.reduce(lambda x, y: x if x > y else y, list)

# Выводим результат
print(result)
