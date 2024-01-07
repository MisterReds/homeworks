
# импортируем библиотеки numpy и matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

# генерируем данные следующим образом
X = np.random.normal(0, 1, 3000)
Y = np.random.normal(3, 4, 3000)

# рисуем точки на плоскости с заданными параметрами
plt.scatter(X, Y, s=10, c='green', marker='.', alpha=0.3)

# добавляем сетку на график
plt.grid()

# подписываем оси координат
plt.xlabel('X')
plt.ylabel('Y')

# добавляем заголовок к рисунку
plt.title('График случайных точек')

# показываем рисунок на экране
plt.show()
