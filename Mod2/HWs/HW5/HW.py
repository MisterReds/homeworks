 # импортируем библиотеку pandas
import pandas as pd

# читаем датасет в датафрейм с указанием разделителя ';'
df = pd.read_csv('Customers.csv', sep=';')

# проверяем данные на наличие пропусков
print(f'Проверка на наличие пропусков:')
print(df.isnull().sum())
# группируем данные по столбцу 'Profession'
df_grouped = df.groupby('Profession')

# находим средний годовой доход в каждой группе
print(f'Средний годовой доход в каждой группе {df_grouped['Income'].mean()}')