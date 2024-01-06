
import numpy as np

# Создаем массив из чисел от 1 до 10
arr = np.arange(1, 11)

# Используем функцию tile для повторения массива по горизонтали 10 раз
matrix = np.tile(arr, (10, 1))

# Выводим результат
print(matrix)
