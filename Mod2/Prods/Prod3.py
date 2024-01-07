# импортируем библиотеки
import pandas as pd
import matplotlib.pyplot as plt

# скачиваем датасет
df = pd.read_csv('Housing.csv', sep=',')

# создаем рисунок с 4 полями
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
fig.tight_layout(pad=3)

# строим график с гостевой комнатой
axes[0, 0].scatter(df['price'], df['area'], c=pd.factorize(df['guestroom'])[0], cmap='bwr', alpha=0.5)
axes[0, 0].legend(['Нет гостевой комнаты', 'Есть гостевая комната'], loc='upper right')
axes[0, 0].set_xlabel('Цена')
axes[0, 0].set_ylabel('Площадь')
axes[0, 0].set_title('График квартир по цене и площади с учетом гостевой комнаты')
axes[0, 0].grid()

# строим график с подвалом
axes[0, 1].scatter(df['price'], df['area'], c=pd.factorize(df['basement'])[0], cmap='bwr', alpha=0.5)
axes[0, 1].legend(['Нет подвала', 'Есть подвал'], loc='upper right')
axes[0, 1].set_xlabel('Цена')
axes[0, 1].set_ylabel('Площадь')
axes[0, 1].set_title('График квартир по цене и площади с учетом подвала')
axes[0, 1].grid()

# строим график с обогревом с помощью горячей воды
axes[1, 0].scatter(df['price'], df['area'], c=pd.factorize(df['hotwaterheating'])[0], cmap='bwr', alpha=0.5)
axes[1, 0].legend(['Нет обогрева с помощью горячей воды', 'Есть обогрев с помощью горячей воды'], loc='upper right')
axes[1, 0].set_xlabel('Цена')
axes[1, 0].set_ylabel('Площадь')
axes[1, 0].set_title('График квартир по цене и площади с учетом обогрева с помощью горячей воды')
axes[1, 0].grid()

# строим график с предбанником
axes[1, 1].scatter(df['price'], df['area'], c=pd.factorize(df['prefarea'])[0], cmap='bwr', alpha=0.5)
axes[1, 1].legend(['Нет предбанника', 'Есть предбанник'], loc='upper right')
axes[1, 1].set_xlabel('Цена')
axes[1, 1].set_ylabel('Площадь')
axes[1, 1].set_title('График квартир по цене и площади с учетом предбанника')
axes[1, 1].grid()

# показываем рисунок
plt.show()
