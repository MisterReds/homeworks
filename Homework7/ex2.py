# Задаем список
numbers = [19, 65, 57, 39, 152, 190, 20, 85, 68, 143]

# Используем filter и lambda для поиска чисел из списка, кратных 19 или 13
result = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))

# Выводим результат
print(result)
