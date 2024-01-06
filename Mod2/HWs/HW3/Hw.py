# Импортируем библиотеки numpy и pandas
import numpy as np
import pandas as pd

# Создаем DataFrame из numpy массива
data = np.random.randint(1, 11, size=(10, 3)) # массив из 10 строк и 3 столбцов со случайными числами от 1 до 10
df = pd.DataFrame(data, columns=['A', 'B', 'C']) # DataFrame с названиями столбцов A, B, C

# Выводим первые и последние 3 строки таблицы
print(df.head(3)) # первые 3 строки
print(df.tail(3)) # последние 3 строки

# Сохраняем DataFrame в csv формат
df.to_csv('my_data.csv', sep=';', encoding='utf-8', index=False) # сохраняем в файл my_data.csv с разделителем ; и кодировкой utf-8 без индексов
