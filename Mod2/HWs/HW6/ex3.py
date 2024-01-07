# импортируем библиотеки numpy и matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

# генерируем данные следующим образом
data = np.random.normal(16, 2, 1000)

# строим гистограмму красного цвета с полупрозрачными столбиками
plt.hist(data, color='red', alpha=0.5)

# подписываем оси координат
plt.xlabel('Время (секунды)')
plt.ylabel('Количество школьников')

# добавляем заголовок к рисунку
plt.title('Гистограмма результатов забега школьников на 100 метров')

# показываем рисунок на экране
plt.show()
