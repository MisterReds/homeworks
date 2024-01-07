# импортируем библиотеки math, numpy и matplotlib.pyplot
import math
import numpy as np
import matplotlib.pyplot as plt

# определяем функцию f(x), которая принимает на вход x и возвращает результат
def f(x):
  # возвращаем результат выражения, используя np.sin вместо math.sin
  return np.sin(x**2) / (x + 1) + np.cos(x) * np.exp(-x)

# задаем диапазон и количество точек для X
x_min = -10
x_max = 10
n_points = 100

# генерируем равномерно распределенные точки для X
X = np.linspace(x_min, x_max, n_points)

# вычисляем Y, применяя функцию f(x) к каждому элементу X
Y = f(X)

# создаем новый рисунок
plt.figure()

# рисуем график функции f(x) с заданными параметрами
plt.plot(X, Y, linestyle='--', color='green', alpha=0.5, label='Вот такая моя функция')

# добавляем сетку на график
plt.grid()

# подписываем оси координат
plt.xlabel('x')
plt.ylabel('f(x)')

# добавляем заголовок к рисунку
plt.title('График сложной алгебраической функции')

# добавляем легенду к графику
plt.legend()

# показываем рисунок на экране
plt.show()
