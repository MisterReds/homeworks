s = input("Введите список чисел через пробел:  ") # вводим строку с числами
n = int(input("Введите натуральное число степени:  ")) # вводим степень
nums = [int(x) for x in s.split()] # преобразуем строку в список чисел
powers = [x**n for x in nums] # возводим каждое число в степень n
print(powers) # выводим результат
