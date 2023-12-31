def sum_of_digits(n):
    # n - заданное число
    sum = 0 # переменная для хранения суммы цифр
    while n != 0: # пока число не равно 0
        remainder = n % 10 # находим остаток от деления на 10
        sum = sum + remainder # прибавляем остаток к сумме
        n = n // 10 # делим число на 10 и отбрасываем дробную часть
    return sum # возвращаем сумму цифр

# Пример использования функции
n = int(input("Введите число:"))

print(sum_of_digits(n)) # выводит 6
