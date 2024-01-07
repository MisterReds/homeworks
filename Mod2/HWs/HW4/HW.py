# импортируем библиотеку pandas
import pandas as pd
# читаем датасет в датафрейм
df = pd.read_csv('Customers.csv', sep=';')

# фильтруем датафрейм по первому условию
df_filtered_1 = df.query("Age > 30 and Income < 30000")

# фильтруем датафрейм по второму условию
df_filtered_2 = df.query("Profession == 'Lawyer' and Work_Experience > 5") # удаляем лишнюю букву l

# выводим результаты
print("Люди, у которых возраст больше 30 и доход меньше 30000:")
print(df_filtered_1)
print("Люди, которые по профессии юристы и с опытом работы больше 5 лет:")
print(df_filtered_2)
