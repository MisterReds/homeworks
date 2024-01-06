import numpy as np

# Создаем массив из 1000 векторов, каждый из которых содержит 100 случайных чисел от 1 до 10
arr = np.random.randint(1, 11, size=(1000, 100))

# Сравниваем каждый элемент массива с 7 и получаем булев массив
bool_arr = arr > 7

# Считаем количество True в каждом векторе и получаем массив из 1000 чисел
count = np.count_nonzero(bool_arr, axis=1)

# Делим каждое число на 100 и умножаем на 100, чтобы получить массив из 1000 процентов
percent = count / 100 * 100

# Сравниваем каждый процент в массиве с 20 и получаем булев массив
bool_percent = percent == 20

# Считаем количество True в булевом массиве и получаем число
count_percent = np.count_nonzero(bool_percent)

# Делим это число на 1000 и умножаем на 100, чтобы получить процент векторов, которые имеют ровно 20% элементов, больших 7
result = count_percent / 1000 * 100

# Выводим результат
print(f"Процент векторов, которые имеют ровно 20% элементов, больших 7, равен {result:.2f}%")