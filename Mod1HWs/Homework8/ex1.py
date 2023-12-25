
# Рекурсивная функция, которая находит максимальное число в списке
def max_number(lst):
  # Базовый случай: если список пуст, вернуть None
  if not lst:
    return None
  # Базовый случай: если список состоит из одного элемента, вернуть этот элемент
  if len(lst) == 1:
    return lst[0]
  # Рекурсивный случай: сравнить первый элемент списка с максимальным числом в оставшейся части списка
  return max(lst[0], max_number(lst[1:]))
print(max_number((input("Введите список чисел:  "))))